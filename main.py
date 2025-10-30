import os
import shutil
from datetime import datetime

# 整理したいフォルダのパス
TARGET_DIR = "./data"

#　拡張子ごとの仕分け先
CATEGORIES = {
  "images":[".jpg", "jpeg",".png", ".gif"],
  "documents":[".pdf","docx","txt"],
  "excel":[".xlsx",".xls",".csv"],
  "archives":[".zip",".rar"], 
}

def organize_files():
    for file in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR,file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False

            #拡張子ごとに仕分け
            for folder, extensions in CATEGORIES.items():
                if ext in extensions:
                    move_to_folder(file_path, folder)
                    moved = True
                    break
                
            # 該当なし→ othersフォルダへ
            if not moved:
                move_to_folder(file_path, "others")

def move_to_folder(file_path, folder_name):
    date_folder = datetime.now().strftime("%Y-%m")
    dest_dir = os.path.join(TARGET_DIR, folder_name, date_folder)
    os.makedirs(dest_dir, exist_ok = True)
    shutil.move(file_path, os.path.join(dest_dir, os.path.basename(file_path)))
    print(f"✅ {os.path.basename(file_path)} → {folder_name}/{date_folder}/")

if __name__ == "__main__":
    organize_files()
    print("ファイル整理が完了しました!")

