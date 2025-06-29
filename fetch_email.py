import imaplib
import email
from email.header import decode_header
import os

def fetch_pdfs(output_dir="downloads"):
    username = "youremail@gmail.com"
    password = "yourapppassword"
    imap_url = "imap.gmail.com"

    os.makedirs(output_dir, exist_ok=True)

    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(username, password)
    mail.select("inbox")

    result, data = mail.search(None, '(UNSEEN SUBJECT "bill" BODY "pdf")')
    mail_ids = data[0].split()

    for num in mail_ids:
        result, msg_data = mail.fetch(num, '(RFC822)')
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            if filename and filename.endswith('.pdf'):
                filepath = os.path.join(output_dir, filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                print(f"[+] Saved: {filepath}")
    mail.logout()
