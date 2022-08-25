import cv2
import matplotlib.pyplot as plt
import skimage
from skimage import measure, morphology
from skimage.color import label2rgb
from skimage.measure import regionprops

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

image = cv2.imread('data/Pan/front2.jpg')
img = image_resize(image, width=600, height = 800)
imgCrop = img[400:650,50:450]
imgWarpGray = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY)
imageT = cv2.threshold(imgWarpGray, 127, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('Threshold',imgWarpGray)
cv2.imshow('Binary',imageT)

cv2.waitKey(0)