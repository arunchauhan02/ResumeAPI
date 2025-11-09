
from pyresparser import ResumeParser
from docx import Document
import os

def ExtractFromResume(text):
    temp_path = 'temp_resume_text.docx'

    # ✅ Properly create a DOCX document
    doc = Document()
    doc.add_paragraph(text)
    doc.save(temp_path)

    data = {}
    try:
        data = ResumeParser(temp_path).get_extracted_data()
    except Exception as e:
        print(f"Error during parsing: {e}")

    if os.path.exists(temp_path):
        os.remove(temp_path)

    return data
