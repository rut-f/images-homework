import numpy as np
import cv2
import matplotlib.pyplot as plt

# ==============================
# פונקציה ליצירת תמונה low contrast
# ==============================
def create_low_contrast_image(height, width, fg, bg):
    """
    יוצרת תמונה בגווני אפור עם ניגוד נמוך
    
    height, width : גודל התמונה
    fg : צבע הרקע
    bg : צבע החזית (הצורה)
    """
    # יוצרים תמונה מלאה בצבע הרקע
    img = np.full((height, width), fg, dtype=np.uint8)
    
    # מציירים עיגול במרכז התמונה
    center = (width // 2, height // 2)
    radius = min(height, width) // 4
    cv2.circle(img, center, radius, bg, -1)  # -1 למילוי העיגול
    
    return img

# ==============================
# פונקציה ל-normalization
# ==============================
def normalize(img):
    """
    מבצעת normalization על תמונת אפור
    כך שהערך המינימלי יהיה 0 והמקסימלי 255
    """
    # המרה ל-float כדי לא לאבד מידע בחישוב
    src_float = img.astype(np.float32)

    min_val = np.min(src_float)
    max_val = np.max(src_float)
    mean_val = np.mean(src_float)

    print(f"Min: {min_val}, Max: {max_val}, Mean: {mean_val}")

    # פקטור למתיחת הערכים
    factor = 255 / (max_val - min_val) if max_val != min_val else 1
    print(f"Factor (255/(max-min)): {factor}")

    # מתיחת ערכי הפיקסלים
    dst_float = (src_float - min_val) * factor

    # המרה חזרה ל-uint8
    dst = np.clip(dst_float, 0, 255).astype(np.uint8)

    return dst

# ==============================
# קוד בדיקה והצגה
# ==============================

# יוצרים תמונה עם ניגוד נמוך
low_contrast_img = create_low_contrast_image(300, 500, fg=100, bg=105)

# מריצים normalization
normalized_img = normalize(low_contrast_img)

# הצגה עם matplotlib
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Low Contrast")
# plt.imshow(low_contrast_img, cmap='gray')
plt.imshow(low_contrast_img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Normalized")
# plt.imshow(normalized_img, cmap='gray')
plt.imshow(normalized_img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.show()
