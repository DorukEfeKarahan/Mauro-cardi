import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('5.jpg')


if image is None:
    print("Böyle bir görsel yok.")
    exit()

def create_pixel_art(image, pixel_size):
    h, w = image.shape[:2]
    small = cv2.resize(image, (W // pixel_size, h // pixel_size), interpolation=cv2.INTER_NEAREST)
    pixel_art = cv2.resize(small, (w,h), interpolation=cv2.INTER_NEAREST)
    return pixel_art

pixel_art_image = create_pixel_art(image, 10)


plt.figure(figsize=(8, 8))
plt.subplot(1, 1, 1)
plt.title('Pixel Art Görseli', fontsize=16, fontweight='bold', color='teal')

plt.inshow(cv2.cvtColor(pixel_art_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tigth_layout()
plt.show()