# resume_parser.py

import os
import json
import pypdf
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

PROMPT_TEMPLATE = "You are an expert resume parser. Given the resume text, extract the following fields and return a single valid JSON object: { "Name": "...", "Email": "...","Phone": "...", "LinkedIn": "...", "Skills": [...], "Education": [...], "Experience": [...], "Projects": [...], "Certifications": [...], "Languages": [...] } Rules:- If a field cannot be found, set its value to 'No idea'. - Return ONLY valid JSON (no extra commentary). - Keep lists as arrays, and keep Experience/Projects as arrays of short strings. Resume text: {text}"

prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["text"])

def load_resume(file_path: str, filename: str):
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif filename.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
    elif filename.endswith(".txt"):
        loader = TextLoader(file_path)
    else:
        return None
    return loader.load()

def ExtractFromResume(file_path: str, filename: str):
    docs = load_resume(file_path, filename)
    if not docs:
        return {"error": "Unsupported file type."}

    full_text = "\n\n".join([d.page_content for d in docs])
    
    formatted_prompt = prompt.format(text=full_text)
    
    response = llm.invoke(formatted_prompt)
    try:
        parsed_json = json.loads(response.content)
        return parsed_json
    except json.JSONDecodeError:
        return {"raw_response": response.content}
