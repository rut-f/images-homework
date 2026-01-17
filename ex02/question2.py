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


def brighten(img, b, func):
    """
    img  : grayscale image
    b    : integer added to each pixel
    func : 'np' or 'cv2'
    """
    if func == "np":
        result = np.add(img, b)
    elif func == "cv2":
        result = cv2.add(img, b)
    else:
        raise ValueError("func must be 'np' or 'cv2'")

    return result

# ===== קוד בדיקה והצגה =====
img = create_gradient_image(300, 500)
bright = brighten(img, 50, "cv2")

plt.imshow(bright, cmap='gray')
plt.axis('off')
plt.show()