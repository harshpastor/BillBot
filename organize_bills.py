import os
import shutil

<<<<<<< HEAD
def save_bill(file_path, category, bill_date, base_dir="bills"):
    os.makedirs(base_dir, exist_ok=True)
    category_folder = os.path.join(base_dir, category)
    os.makedirs(category_folder, exist_ok=True)

    filename = f"{bill_date.strftime('%Y-%m-%d')}_{os.path.basename(file_path)}"
    dest_path = os.path.join(category_folder, filename)

    counter = 1
    while os.path.exists(dest_path):
        filename = f"{bill_date.strftime('%Y-%m-%d')}_{counter}_{os.path.basename(file_path)}"
        dest_path = os.path.join(category_folder, filename)
        counter += 1

    shutil.move(file_path, dest_path)
    print(f"[✓] Saved bill to: {dest_path}")
=======
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
>>>>>>> 37488f3306ac7fb320daf90c4064b4a9967cacda
