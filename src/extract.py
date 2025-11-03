import pdfplumber

def extract_sections(path):
    sections = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue
            paras = [p.strip() for p in text.split('\n\n') if p.strip()]
            for p in paras:
                sections.append({'title': None, 'text': p, 'page': i+1})
    return sections
