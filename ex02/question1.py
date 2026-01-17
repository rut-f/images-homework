import numpy as np
import cv2
import matplotlib.pyplot as plt

def create_gradient_image(height, width):
    img = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            value = int((x + y) * 255 / (width + height - 2))
            img[y, x] = value

    return img

# קוד ראשי – יצירה והצגה
img = create_gradient_image(300, 500)

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
