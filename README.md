# BillBot
A smart assistant automating your bills
Here's a professional and well-structured **`README.md`** for your project **BillBot**:

---

# 🤖 BillBot — Your Personal Bill Organizer

**BillBot** is a smart automation platform that extracts PDF bills from your email, identifies the bill type and date using intelligent parsing, and organizes them into structured folders — automatically!

No more digging through inboxes or scattered downloads — BillBot sorts your life, one bill at a time.

---

## 🚀 Features

- 📥 Automatically fetches PDF bills from your email inbox
- 🧾 Parses bill content and extracts key metadata (bill type, date)
- 🧠 Classifies bills using rule-based logic (Electricity, Water, Mobile, etc.)
- 📂 Organizes files into folders by type and month (`bills/electricity/2025-06.pdf`)
- 🔍 Optional OCR support for scanned/image-based PDFs
- 🌐 Web dashboard to view & trigger scans (Flask-based)
- ⏱️ Cron or Celery-ready for automation

---

## 📦 Folder Structure

`
billbot/
├── fetch\_emails.py          # Download PDFs from email
├── parse\_pdf.py             # Extract text or OCR
├── classify\_bill.py         # Identify type and date
├── organize\_bills.py        # Save into correct folders
├── main.py                  # Run the full pipeline
├── requirements.txt
├── templates/               # (For Flask dashboard)
├── static/                  # (Optional assets)
└── README.md

````

---

## 🧰 Tech Stack

| Purpose            | Tech                         |
|--------------------|------------------------------|
| Email Integration  | `imaplib`, Gmail API         |
| PDF Parsing        | `pdfplumber`, `PyMuPDF`      |
| OCR (optional)     | `pdf2image`, `pytesseract`   |
| Bill Classification| Python regex / NLP           |
| Dashboard (optional)| Flask + HTML/CSS            |
| Automation         | `cron`, `Celery`             |
| Deployment         | Docker, Heroku, GCP, etc.    |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/billbot.git
cd billbot
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

For OCR support:

```bash
sudo apt install tesseract-ocr poppler-utils
pip install pytesseract pdf2image
```

### 3. Configure Email Access

Create `config/email_config.json`:

```json
{
  "email": "youremail@gmail.com",
  "password": "your-app-password",
  "imap_server": "imap.gmail.com"
}
```

⚠️ Use [App Passwords](https://support.google.com/accounts/answer/185833) if using Gmail with 2FA.

---

## ▶️ Run the Automation Pipeline

```bash
python main.py
```

This will:

* Fetch new PDFs from your inbox
* Extract content
* Classify and organize them into folders

---

## 🌐 Web Dashboard (Optional)

```bash
export FLASK_APP=app.py
flask run
```

Access the dashboard at `http://127.0.0.1:5000/`

---

## 🐳 Docker Support

Build the image:

```bash
docker build -t billbot .
```

Run the container:

```bash
docker run -v $(pwd)/bills:/app/bills billbot
```

---
UML Design:
![image](https://github.com/user-attachments/assets/e480308b-8f49-4264-a580-a964688f17a4)

## 🧠 Future Enhancements

* [ ] ML-powered bill classification
* [ ] Integration with Google Drive / Dropbox
* [ ] User accounts and role-based access
* [ ] SMS/Email alerts on bill arrival

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.


---

## 🔗 Links

* 🔧 [Leetcode Profile](https://leetcode.com/harshpastor/)
* 💼 [LinkedIn](https://linkedin.com/in/harshpastor)
* 📂 [Project Demo (coming soon)]()

---

> *BillBot — Organize, classify, and conquer your inbox chaos!*
