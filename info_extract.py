

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
import sys


def temp(file_path: str, name: str): 
    # Load the text file
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split the documents into smaller chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings()
    db = Chroma.from_documents(texts, embeddings)
    retriever = db.as_retriever(search_kwargs={'k': 2})
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = HuggingFaceHub(huggingfacehub_api_token='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',
                        repo_id=repo_id, model_kwargs={"temperature":0.2, "max_new_tokens":200})
    qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever,return_source_documents=True)

    chat_history = []

    # Define the filename for storing the information
    filename = "llm_answer/mno.txt"

    # Define a function to save the information to a text file
    def save_information(data):
        with open(filename, 'w') as file:
            for query, answer in data.items():
                file.write(f"Question: {query}\n")
                file.write(f"Answer: {answer}\n\n")

    # Initialize an empty dictionary to store the information
    stored_information = {}

    # Define multiple preset queries
    preset_queries = [
        "Provide Educational Details",
        "Provide Work Experience",
        "Provide all the Projects",
        "Extract all the Job Titles from work experience with timeline", 
        "Give only all the Job Titles"
    ]

    # Iterate over preset queries and store the results
    counter = 0
    for query in preset_queries:
        result = qa_chain({'question': query, 'chat_history': chat_history})
        answer = result['answer']
        helpful_index = answer.find("Helpful Answer:")
        if helpful_index != -1:
            answer = answer[helpful_index+len("Helpful Answer:"):]

        stored_information[query] = answer.strip()

        # Print and store the information
        print('Question:', query)
        print('Answer:', stored_information[query] + '\n')
        temp_file = open(f"llm_answer/{name}-{counter}.txt", 'w')
        temp_file.write(stored_information[query])
        counter = counter + 1

