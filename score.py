import cv2
import numpy as np
import pandas as pd
#from skimage import io, img_as_float


# import imquality.brisque as brisque

def get_blurrness_score(image):
    # image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(image, cv2.CV_64F).var()
    return fm // 100


def average_pixel_width(img):
    # img = cv2.imread(image)
    t_lower = 100
    t_upper = 200
    aperture_size = 5
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_array = np.asarray(img_gray)
    edges_sigma1 = cv2.Canny(im_array, t_lower, t_upper, apertureSize=aperture_size)
    apw = (float(np.sum(edges_sigma1)) / (img.shape[0] * img.shape[1]))
    return apw


def sharpness_score(img):
    # img = cv2.imread(image)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    gnorm = np.sqrt(laplacian ** 2)
    sharpness = np.average(gnorm)
    return sharpness


def centroid(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image, 127, 255, 0)
    M = cv2.moments(thresh)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    return [cX, cY]


img = cv2.imread("12.jpeg")

# imgResize = cv2.resize(img,(400,60)
cv2.imshow("Output", img)
# score = color_analysis(img)
print(get_blurrness_score(img), average_pixel_width(img), sharpness_score(img))
cv2.waitKey(0)

