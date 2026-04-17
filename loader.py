# loader.py

import fitz  # PyMuPDF


def load_txt(file):
    """
    Reads uploaded text file safely from memory
    """

    try:
        # Read bytes
        file_bytes = file.read()

        # Decode safely (handles weird encodings)
        text = file_bytes.decode("utf-8", errors="ignore")

        return text

    except Exception as e:
        raise Exception(f"Error reading TXT file: {str(e)}")


def load_pdf(file):
    """
    Reads uploaded PDF file directly from memory
    """

    try:
        # Read PDF bytes
        pdf_bytes = file.read()

        # Open PDF from memory
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        text = ""

        # Extract text page by page
        for page in doc:
            text += page.get_text()

        return text

    except Exception as e:
        raise Exception(f"Error reading PDF file: {str(e)}")