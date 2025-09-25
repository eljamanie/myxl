import json
import os

HOT1_PATH = "data/pg-hot.json"
HOT2_PATH = "data/pg-hot2.json"
COMBINED_PATH = "data/hot_combined.json"

def main():
    if not os.path.exists(HOT1_PATH):
        print(f"File {HOT1_PATH} tidak ditemukan!")
        return
    if not os.path.exists(HOT2_PATH):
        print(f"File {HOT2_PATH} tidak ditemukan!")
        return

    # Baca data pg-hot.json
    with open(HOT1_PATH, "r", encoding="utf-8") as f:
        hot1 = json.load(f)
    # Baca data pg-hot2.json
    with open(HOT2_PATH, "r", encoding="utf-8") as f:
        hot2 = json.load(f)

    # Tambahkan penanda tipe
    hot1_tagged = []
    for item in hot1:
        item["type"] = "hot1"
        hot1_tagged.append(item)
    hot2_tagged = []
    for item in hot2:
        item["type"] = "hot2"
        hot2_tagged.append(item)

    # Gabung array
    combined = hot1_tagged + hot2_tagged

    # Simpan ke file gabungan
    with open(COMBINED_PATH, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print(f"Berhasil digabung ke {COMBINED_PATH}")

if __name__ == "__main__":
    main()