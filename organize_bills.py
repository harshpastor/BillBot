import os
import shutil

def organize(pdf_path, bill_type, bill_date, dest_root="bills"):
    if bill_date:
        filename = bill_date.strftime("%Y-%m") + ".pdf"
    else:
        filename = os.path.basename(pdf_path)

    folder = os.path.join(dest_root, bill_type)
    os.makedirs(folder, exist_ok=True)

    new_path = os.path.join(folder, filename)
    shutil.move(pdf_path, new_path)
    print(f"[✓] Moved to: {new_path}")
