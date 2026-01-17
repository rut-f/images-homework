import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ==============================
# קריאת תמונה (נתיב בעברית אפשרי)
# ==============================
# image_path = r"C:\Users\The user\Desktop\מכללה\עיבוד תמונה נדב אהרוני\ex02\image.jpg"
image_path = "image.jpg" #כדי שירוץ גם בגיט
img = Image.open(image_path)

# ==============================
# המרה לגווני אפור
# ==============================
img_gray = img.convert("L")
img_gray_np = np.array(img_gray)

# ==============================
# חישוב היסטוגרמה ידני
# ==============================
hist = np.zeros(256, dtype=int)
for value in img_gray_np.flatten():
    hist[value] += 1

# ==============================
# הצגה: תמונה + היסטוגרמה
# ==============================
plt.figure(figsize=(12,5))

# תמונה בגווני אפור
plt.subplot(1,2,1)
plt.imshow(img_gray_np, cmap='gray', vmin=0, vmax=255)
plt.title("Grayscale Image")
plt.axis('off')

# היסטוגרמה
plt.subplot(1,2,2)
plt.bar(range(256), hist, color='gray')
plt.title("Histogram")
plt.xlabel("Pixel Value (0-255)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
