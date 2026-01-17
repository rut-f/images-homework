import numpy as np
import cv2
import matplotlib.pyplot as plt


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


# ===== קוד בדיקה והצגה =====

# יוצרים תמונה עם ניגוד נמוך
low_contrast_img = create_low_contrast_image(300, 500, fg=100, bg=105)

# הצגה

plt.imshow(low_contrast_img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.title("Low Contrast Image (fg=100, bg=105)")
plt.show()
