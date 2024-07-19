import os
import fitz  # PyMuPDF
import docx
from PIL import Image
import pytesseract
from bs4 import BeautifulSoup
import tifffile
from pylatexenc import latexwalker, latex2text, macrospec

# Function to convert PDF to text
def pdf_to_text(pdf_file):
    text = ""
    with fitz.open(pdf_file) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Function to convert DOCX to text
def docx_to_text(docx_file):
    text = ""
    doc = docx.Document(docx_file)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Function to convert JPG to text
def image_to_text(image_file):
    print("Yes im here!!")
    text = ""
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    print(text)
    return text

# Function to convert HTML to text
def html_to_text(html_file):
    with open(html_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        text = soup.get_text()
    return text

# Function to convert TXT to text
def txt_to_text(txt_file):
    with open(txt_file, "r") as file:
        text = file.read()
    return text

# Function to convert LaTeX to text
def latex_to_text(latex_file):
    with open(latex_file, "r", encoding="utf-8") as file:
        latex_content = file.read()
        text = latex2text.latex2text(latex_content)
    return text

# Function to determine file type and convert to text
def convert_to_text(file_path, name):
    print(file_path)
    text = ""
    file_extension = file_path.split(".")[-1].lower()
    print(file_extension)
    if file_extension == "pdf":
        text = pdf_to_text(file_path)
    elif file_extension == "docx":
        print(file_path)
        text = docx_to_text(file_path)
    elif file_extension in ["jpg", "jpeg", "png", "tiff"]:
        text = image_to_text(file_path)
    elif file_extension == "html":
        text = html_to_text(file_path)
    elif file_extension == "tex":
        text = latex_to_text(file_path)
    elif file_extension == "txt":
        text = txt_to_text(file_path)
    else:
        return "Unsupported file format."

    file1 = open(f'output/{name}.txt','w', encoding="utf-8")
    file1.write(text)
    file1.close()