import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import os

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from PDFs; falls back to OCR if image-based.
    Returns structured sections for slide creation.
    """
    sections = []
    full_text = ""

    print("📄 Extracting text from PDF...")

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            full_text += text + "\n"

    # OCR fallback
    if not full_text.strip():
        print("⚠️ No selectable text found, running OCR...")
        images = convert_from_path(pdf_path)
        for img in images:
            full_text += pytesseract.image_to_string(img) + "\n"

    if not full_text.strip():
        print("❌ No text could be extracted.")
        return [{"title": "No text extracted", "content": "PDF may be image-based or empty."}]

    keywords = [
        "Education", "Projects", "Experience", "Skills",
        "Summary", "Certifications", "Work Experience",
        "Achievements", "Publications", "Internships"
    ]

    lines = full_text.splitlines()
    current = {"title": "Section 1", "content": ""}

    for line in lines:
        clean = line.strip()
        if not clean:
            continue
        if any(k.lower() in clean.lower() for k in keywords):
            if current["content"]:
                sections.append(current)
            current = {"title": clean, "content": ""}
        else:
            current["content"] += clean + " "

    if current["content"]:
        sections.append(current)
    print(f"✅ Extracted {len(sections)} sections from {os.path.basename(pdf_path)}")

    return sections


# Alias for pipeline compatibility
extract_sections_from_pdf = extract_text_from_pdf
