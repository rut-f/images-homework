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
    if func == "np":
        result = np.add(img, b)
    elif func == "cv2":
        result = cv2.add(img, b)
    else:
        raise ValueError("func must be 'np' or 'cv2'")
    return result


# ===== קוד בדיקה והצגה =====

# יוצרים את תמונת הגרדיאנט
img = create_gradient_image(300, 500)

# מפעילים brighten פעמיים עם ערכים שונים ל-func
bright_np = brighten(img, 50, "np")
bright_cv2 = brighten(img, 50, "cv2")

# הצגה עם matplotlib
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Brighten np.add")
plt.imshow(bright_np, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Brighten cv2.add")
plt.imshow(bright_cv2, cmap='gray')
plt.axis('off')

plt.show()
