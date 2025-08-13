# ui.py
import tkinter as tk
from tkinter import messagebox
from email_fetcher import fetch_pdfs
from provider_help import get_provider_info

def create_ui():
    root = tk.Tk()
    root.title("Bill Fetcher")

    tk.Label(root, text="Email:").grid(row=0, column=0, sticky="e")
    tk.Label(root, text="Password / App Password:").grid(row=1, column=0, sticky="e")

    email_entry = tk.Entry(root, width=30)
    pass_entry = tk.Entry(root, width=30, show="*")

    email_entry.grid(row=0, column=1)
    pass_entry.grid(row=1, column=1)

    def on_fetch():
        email_val = email_entry.get()
        pass_val = pass_entry.get()

        provider_info = get_provider_info(email_val)
        imap_server = provider_info["imap"] if provider_info else None

        if not imap_server:
            messagebox.showerror("Error", "Unsupported email provider. Please enter IMAP server manually.")
            return

        try:
            msg = fetch_pdfs(email_val, pass_val, imap_server)
            messagebox.showinfo("Success", msg)
        except Exception as e:
            messagebox.showerror("Login Failed", str(e))

    tk.Button(root, text="Fetch Bills", command=on_fetch).grid(row=2, columnspan=2, pady=10)

    root.mainloop()
