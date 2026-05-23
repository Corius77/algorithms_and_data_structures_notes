from pypdf import PdfReader

def extract_with_pypdf(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    
    for page in reader.pages:
        # Metoda extract_text() wyciąga surowy tekst ze strony
        full_text += page.extract_text() + "\n"
        
    return full_text

if __name__ == "__main__":
    tekst = extract_with_pypdf('biblia.pdf')
    print(tekst)