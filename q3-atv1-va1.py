import os
import random
from PIL import Image

def crop_image(image_path: str, width: int, height: int, output_path: str):
    img = Image.open(image_path)
    img_width, img_height = img.size

    left = 0
    top = 0
    right = min(width, img_width)
    bottom = min(height, img_height)

    cropped = img.crop((left, top, right, bottom))
    cropped.save(output_path)
    print(f"Imagem recortada salva em: {output_path}")

data_dir = "data"
valid_exts = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
files = [f for f in os.listdir(data_dir) if f.lower().endswith(valid_exts)]

if files:
    chosen_file = random.choice(files)
    path = os.path.join(data_dir, chosen_file)
    output_path = os.path.join(data_dir, f"cropped_{chosen_file}")
    crop_image(path, 100, 100, output_path)
else:
    print("Nenhuma imagem encontrada no diretório data/")
