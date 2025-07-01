from fetch_emails import fetch_pdfs
from parse_pdf import extract_text
from classify_bill import classify
from organize_bills import organize
import os

def run_pipeline():
    fetch_pdfs("downloads")
    for filename in os.listdir("downloads"):
        if not filename.endswith(".pdf"):
            continue
        path = os.path.join("downloads", filename)
        text = extract_text(path)
        bill_type, bill_date = classify(text)
        organize(path, bill_type, bill_date)

if __name__ == "__main__":
    run_pipeline()
