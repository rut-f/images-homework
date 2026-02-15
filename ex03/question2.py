import sys
import cv2
import numpy as np

# קריאת קלט מהמשתמש
R = int(sys.argv[1])
G = int(sys.argv[2])
B = int(sys.argv[3])

# נורמליזציה ל-0..1 עבור חישובים ידניים
r = R / 255
g = G / 255
b = B / 255

# חישוב ידני של HSV
Cmax = max(r, g, b)
Cmin = min(r, g, b)
delta = Cmax - Cmin

# Hue
if delta == 0:
    H_hsv = 0
elif Cmax == r:
    H_hsv = 60 * (((g - b) / delta) % 6)
elif Cmax == g:
    H_hsv = 60 * (((b - r) / delta) + 2)
else:
    H_hsv = 60 * (((r - g) / delta) + 4)

# Saturation
S_hsv = 0 if Cmax == 0 else delta / Cmax

# Value
V_hsv = Cmax

# חישוב ידני של HSL
L = (Cmax + Cmin) / 2

if delta == 0:
    S_hsl = 0
else:
    S_hsl = delta / (1 - abs(2 * L - 1))

H_hsl = H_hsv  # אותו חישוב בדיוק כמו ב-HSV

# חישוב ידני של YCrCb
Y  =  0.299*R + 0.587*G + 0.114*B
Cr = (R - Y) * 0.713 + 128
Cb = (B - Y) * 0.564 + 128

# חישוב בעזרת OpenCV
pixel = np.uint8([[[B, G, R]]])  # OpenCV עובד ב-BGR
hsv_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]
hsl_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HLS)[0][0]
ycrcb_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2YCrCb)[0][0]

# הדפסת תוצאות
print("\n--- חישוב ידני ---")
print("HSV:", (H_hsv, S_hsv, V_hsv))
print("HSL:", (H_hsl, S_hsl, L))
print("YCrCb:", (Y, Cr, Cb))

print("\n--- OpenCV ---")
print("HSV:", hsv_cv)
print("HSL:", hsl_cv)
print("YCrCb:", ycrcb_cv)