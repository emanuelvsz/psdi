import cv2
from PIL import Image
import os

data_dir = "data"
valid_exts = (".png")
files = [f for f in os.listdir(data_dir) if f.lower().endswith(valid_exts)]

for file in files:
    path = os.path.join(data_dir, file)

    img_rgb = Image.open(path).convert("RGB")
    img_rgb.show(title=f"{file} - RGB")

    img_gray = img_rgb.convert("L")
    img_gray.show(title=f"{file} - Grayscale")

    img_bgr = cv2.imread(path)
    if img_bgr is not None:
        cv2.imshow(f"{file} - BGR", img_bgr)
        cv2.waitKey(500)
    else:
        print(f"Erro ao carregar {file} em BGR")

cv2.destroyAllWindows()
