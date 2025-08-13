from email_fetcher import fetch_pdfs
from classify_bill import classify_and_get_date
from organize_bills import save_bill

def process_emails(email, password, imap_url):
    print("[*] Connecting to email...")
    pdf_files = fetch_pdfs(email, password, imap_url)

    print(f"[*] Found {len(pdf_files)} bill PDFs")
    for file_path in pdf_files:
        category, bill_date = classify_and_get_date(file_path)
        save_bill(file_path, category, bill_date)
