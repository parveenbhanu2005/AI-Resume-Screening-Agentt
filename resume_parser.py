import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """
    text = ""

    try:
        pdf = fitz.open(pdf_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()

    except Exception as e:
        print(f"Error reading PDF: {e}")

    return text


if __name__ == "__main__":
    pdf_path = "resumes/BHANU.pdf"

    text = extract_text_from_pdf(pdf_path)

    print("=" * 60)
    print("RESUME CONTENT")
    print("=" * 60)
    print(text)