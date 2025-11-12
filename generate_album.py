from pathlib import Path

output_dir = Path("albumy")
output_dir.mkdir(exist_ok=True)

pdf_path = output_dir / "album.pdf"
jpg_path = output_dir / "album.jpg"

with open(pdf_path, "w") as f:
    f.write("Testowy plik PDF")
with open(jpg_path, "w") as f:
    f.write("Testowy plik JPG")

print("✅ Album wygenerowany pomyślnie!")
