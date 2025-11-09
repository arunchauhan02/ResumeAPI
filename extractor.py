from pyresparser import ResumeParser
from docx import Document
import os

def ExtractFromResume(input_file_path):
    try:
        doc = Document()
        with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as f:
            doc.add_paragraph(f.read())
        temp_docx = 'text.docx'
        doc.save(temp_docx)
        data = ResumeParser(temp_docx).get_extracted_data()
        if os.path.exists(temp_docx):
            os.remove(temp_docx)
        return data.get('skills', [])
    except:
        data = ResumeParser(input_file_path).get_extracted_data()
        return data.get('skills', [])
