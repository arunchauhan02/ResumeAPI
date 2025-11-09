

from pyresparser import ResumeParser
import os

def ExtractFromResume(text):
    temp_path = 'temp_resume_text.docx'

    # Save the input text temporarily
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(text)

    data = {}
    try:
        data = ResumeParser(temp_path).get_extracted_data()
    except Exception as e:
        print(f"Error during parsing: {e}")

    # Clean up temporary file
    if os.path.exists(temp_path):
        os.remove(temp_path)

    # Return only the skills list
    return data
