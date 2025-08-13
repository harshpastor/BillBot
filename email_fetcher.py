# email_fetcher.py
import imaplib
import email
import os
from provider_help import get_provider_info

def fetch_pdfs(username, password, imap_url, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    try:
        mail = imaplib.IMAP4_SSL(imap_url)
        mail.login(username, password)
    except imaplib.IMAP4.error:
        provider_info = get_provider_info(username)
        if provider_info:
            raise Exception(f"Login failed.\n\n{provider_info['instructions']}")
        else:
            raise Exception("Login failed. Unknown provider — please check your IMAP settings.")

    mail.select("inbox")
    result, data = mail.search(None, '(UNSEEN SUBJECT "bill" BODY "pdf")')
    mail_ids = data[0].split()

    if not mail_ids:
        return "No new bill emails found."

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
    return f"Downloaded {len(mail_ids)} bill(s)."
