
import os
import re
from docx import Document

def clean_text(text):
    # remove all non-ascii characters
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    # remove all characters that are not letters
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    # remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # remove leading and trailing spaces
    text = text.strip()
    return text

def load_docx(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

def save_text(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def word_to_txt(input_file, output_file):
    text = load_docx(input_file)
    text = clean_text(text)
    save_text(output_file, text)

# Get the current working directory (assumed to be the root of the repository)
repo_root = os.getcwd()

# Define the relative paths
input_file = os.path.join(repo_root, 'my_data', 'Resume_updated.docx')
output_file = os.path.join(repo_root, 'my_data', 'input.txt')

word_to_txt(input_file, output_file)

