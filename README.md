![Resume Revealer Home Page](https://github.com/404-Definitely-Found/Mined-Hackathon-NetRunner/assets/92706697/9beddfef-f712-4f40-b61f-1280258a1ff0)
# Resume Revealer 

Resume Revealer is a web-based application designed to streamline the resume analysis process for both users and HR personnel. The application allows users to upload their resumes, which are then analyzed to extract key information such as skills and experiences. HR personnel can also use the application to review uploaded resumes and assess their suitability for specific job positions based on skill matching.


## Problem statement

### Primary challenge
Develop a comprehensive resume parser, "ResumeRevealer," capable of extracting detailed information from resumes in various formats (PDF, JPG, HTML, DOC, etc.). The parser should accurately classify text into distinct sections (e.g., education, work experience, skills) and sequence them based on dates, where available.


### Standardization challenge
Enhance the "ResumeRevealer" to standardize different job titles and occupations against the O-NET database, ensuring a consistent taxonomy across parsed resumes.
## Installation and Setup

### Prerequisites
For all the dependencies refer to the requirements.txt file
### Database

The application utilizes SQLite for storing and managing data related to user uploads, resume analysis results, and job position selections by HR personnel.


#### Features

- **Data Storage**: Resumes uploaded by users and analysis results are stored in the SQLite database.
- **Efficiency**: SQLite offers lightweight and efficient storage, making it suitable for small to medium-sized applications.
- **Reliability**: Built-in transaction support and ACID compliance ensure data integrity and reliability.
- **Scalability**: While SQLite is primarily designed for single-user applications, it can handle concurrent access from multiple users efficiently.
- **Ease of Use**: Simple setup and management make SQLite a convenient choice for small-scale applications like Resume Revealer.


### Installation
1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/resume-revealer.git

2. Navigate to the project directory:

   ``` bash
   cd resume-revealer

3. Install the required dependencies using pip:
 
   ``` bash
   pip install -r requirements.txt

## Core Features


| Feature                | Description                                                                                       |
|------------------------|---------------------------------------------------------------------------------------------------|
| User-friendly Interface | Intuitive web interface for seamless interaction with the application.                            |
| Resume Upload          | Users can easily upload their resumes in various formats for analysis.                             |
| Resume Analysis        | Automatic extraction of text from uploaded resumes for detailed analysis.                          |
| Skill Extraction       | Identification and extraction of skills mentioned in the resumes.                                   |
| Job Position Selection | HR personnel can select job positions to view uploaded resumes and assess candidate suitability.   |
| Resume Ranking         | Resumes are ranked based on skill matching scores to assist HR personnel in candidate evaluation. |

## Usage

#### For Users

1. **Upload Resume**:
   - Visit the application website.
   - Navigate to the "Upload Resume" section.
   - Click on the "Upload" button and select the resume file you want to analyze.

2. **Resume Analysis**:
   - Once the resume is uploaded, it will be automatically processed.
   - The application will extract the text from the resume file, regardless of its format.
   - Users can then view the extracted text and proceed to submit their queries or questions.

3. **Querying Resume Information**:
   - Users can interact with the application using a chat interface.
   - Common queries include requesting a list of skills mentioned in the resume or asking for a summary of the resume content.

4. **Viewing Results**:
   - After submitting a query, users will receive the results directly in the chat interface.
   - They can review the information provided and continue interacting with the application as needed.
   - The application may offer suggestions or insights based on the analysis of the resume content.

#### For HR (Human Resources)

1. **Select Job Position**:
   - HR personnel can access the application website.
   - They will be presented with a list of available job positions or roles.

2. **View Uploaded Resumes**:
   - HR personnel can select a specific job position to view uploaded resumes for that position.
   - The resumes will be displayed along with their rankings based on skill matching according to the job description.

3. **Analyze Resumes**:
   - Resumes are automatically processed upon upload.
   - The application extracts text from the resumes and matches the skills mentioned with those required for the job position.

4. **Review Ranking and Skill Matching**:
   - HR personnel can review the rankings and skill matching scores of the uploaded resumes.
   - This information helps in identifying the most suitable candidates for the job position.

5. **Take Further Action**:
   - Based on the analysis and rankings, HR personnel can take further action such as scheduling interviews or contacting candidates.
