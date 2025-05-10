import os
from PyPDF2 import PdfReader

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'md'}

def extract_text(filepath):
    ext = filepath.rsplit('.', 1)[1].lower()
    if ext == 'pdf':
        reader = PdfReader(filepath)
        return '\n'.join(page.extract_text() or '' for page in reader.pages)
    elif ext == 'md':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ''
