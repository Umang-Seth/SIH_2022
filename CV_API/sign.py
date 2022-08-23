
import cv2
import numpy as np

#read image
rgb_img = cv2.imread('C:/Users/mangl/PycharmProjects/djangouploads/cropped.jpg')
rgb_img = cv2.resize(rgb_img, (900, 600))
gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)

#canny edge detection
canny = cv2.Canny(gray_img, 50, 120)
kernel = np.ones((7, 23), np.uint8)
closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
contours, hierarchy = cv2.findContours(closing.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Sort Contors by area and then remove the largest frame contour
n = len(contours) - 1
contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]

#take a copy
copy = rgb_img.copy()

# Iterate through contours and draw the convex hull
for c in contours:
    if cv2.contourArea(c) < 750:
        continue
    hull = cv2.convexHull(c)
    cv2.drawContours(copy, [hull], 0, (0, 255, 0), 2)
    cv2.imshow('Convex Hull', copy)

cv2.waitKey(0)