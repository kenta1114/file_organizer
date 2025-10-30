import os

def make_sample_files():
    os.makedirs("data", exist_ok = True)

    samples = {
        "data/sample.pdf": "%PDF-1.4\n%Fake PDF file for testing\n",
        "data/sample.xlsx": "Excel test content",
        "data/sample.jpg": "JPEG data simulation",
        "data/sample.txt": "This is a sample text file.",
    }

    for path, content in samples.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    print("✅ サンプルファイルを作成しました！ 'data/' フォルダを確認してください。")

if __name__ == "__main__":
    make_sample_files()

    