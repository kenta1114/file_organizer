import os
import shutil
from datetime import datetime

#提出用フォルダ名
submission_dir = "submission_package"
zip_name = "file_organizer_submission"

#対象ファイル・フォルダ
include_items = [
  "main.py",
  "make_sample_files.py",
  "README.md",
  "data", #サンプルデータ
]

#　古いフォルダがある場合は削除
if os.path.exists(submission_dir):
    shutil.rmtree(submission_dir)

#提出用フォルダを作成
os.makedirs(submission_dir, exist_ok = True)

# 指定ファイルをコピー
for item in include_items:
    if os.path.exists(item):
        dest = os.path.join(submission_dir, item)
        if os.path.isdir(item):
            shutil.copytree(item,dest)
        else:
            shutil.copy2(item, dest)
        print(f"✅ {item} をコピーしました。")
    else:
        print(f"⚠️ {item} が見つかりません。")

# ZIP圧縮
shutil.make_archive(zip_name, 'zip', submission_dir)

print("\n🎉 提出用ZIPを作成しました！")
print(f"📦 出力ファイル: {zip_name}.zip")

#タイムスタンプを表示
print(f"🕒 作成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")