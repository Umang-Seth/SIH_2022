import cv2
import os
import time

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

img = cv2.imread("data/Aadhar/front.jpg")
image = image_resize(img, width=600, height = 800)
#blur = cv2.GaussianBlur(image,(1,1),0)
#blur2 = cv2.GaussianBlur(image,(1,1),50)
median1 = cv2.medianBlur(image,1)
median2 = cv2.medianBlur(image,2)
median3 = cv2.medianBlur(image,3)
median4 = cv2.medianBlur(image,4)
median5 = cv2.medianBlur(image,5)

cv2.imshow("image_new",image)
cv2.imshow("median1",median1)
cv2.imshow("median1",median1)
cv2.imshow("median1",median1)
cv2.imshow("median1",median1)
cv2.imshow("median1",median1)


cv2.waitKey(0)