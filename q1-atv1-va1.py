from PIL import Image

img_black = Image.new("RGB", (28, 28), color="black")
img_black.save("image_black_28x28.png")

img_blue = Image.new("RGB", (256, 256), color=(0, 102, 204))
img_blue.save("image_blue_256x256.png")

print("Imagens salvas: image_black_28x28.png e image_blue_256x256.png")