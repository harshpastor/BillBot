import os
import shutil

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

