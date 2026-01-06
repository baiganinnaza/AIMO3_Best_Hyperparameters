import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pypdf
except ImportError:
    print("pypdf not found, installing...")
    install("pypdf")
    import pypdf

pdf_path = "AIMO3_Reference_Problems (1).pdf"

try:
    reader = pypdf.PdfReader(pdf_path)
    print(f"Number of pages: {len(reader.pages)}")
    
    full_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"--- Page {i+1} ---")
        print(text)
        full_text += text + "\n"
        
except Exception as e:
    print(f"Error reading PDF: {e}")
