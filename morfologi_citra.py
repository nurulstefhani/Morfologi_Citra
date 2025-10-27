import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Baca gambar dan ubah ke grayscale
image = cv2.imread('gambar.jpeg', cv2.IMREAD_GRAYSCALE)

# 2. Konversi ke citra biner
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 3. Buat structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# 4. Operasi morfologi
erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel)

# 5. Tampilkan hasil
titles = ['Original', 'Erosion', 'Dilation', 'Opening', 'Closing', 'Gradient', 'Top Hat', 'Black Hat']
images = [binary, erosion, dilation, opening, closing, gradient, tophat, blackhat]

plt.figure(figsize=(15,10))
for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
