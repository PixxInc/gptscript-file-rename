import os
import sys
from PyPDF2 import PdfReader

def extract_text_from_first_page(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        if len(reader.pages) > 0:
            first_page = reader.pages[0]
            return first_page.extract_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return None

def generate_new_filename(text):
    if text:
        # Extract the first 5 words from the text for the filename
        words = text.split()
        if len(words) >= 5:
            return '_'.join(words[:5]) + '.pdf'
        else:
            return '_'.join(words) + '.pdf'
    return None

def rename_pdf_file(original_path, new_name):
    directory = os.path.dirname(original_path)
    new_path = os.path.join(directory, new_name)
    try:
        os.rename(original_path, new_path)
        print(f"Renamed '{original_path}' to '{new_path}'")
    except Exception as e:
        print(f"Error renaming file: {e}")

if __name__ == "__main__":
    pdf_path = os.getenv('PDF_PATH')
    if not pdf_path:
        print("PDF_PATH environment variable is not set.")
        sys.exit(1)

    text = extract_text_from_first_page(pdf_path)
    new_filename = generate_new_filename(text)
    if new_filename:
        rename_pdf_file(pdf_path, new_filename)
    else:
        print(f"Could not generate a new filename for '{pdf_path}'")
