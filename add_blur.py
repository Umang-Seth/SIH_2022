import cv2
import os
import time
from score import get_blurrness_score
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
myPath = "data/Aadhar/"
img = cv2.imread(str(myPath)+'back.jpg')
image = image_resize(img, width=600, height = 800)

blur3 = cv2.blur(image,(3,3))
blur5 = cv2.blur(image,(5,5))
blur7 = cv2.blur(image,(7,7))

Gblur3 = cv2.GaussianBlur(image,(3,3),0)
Gblur5 = cv2.GaussianBlur(image,(5,5),0)
Gblur7 = cv2.GaussianBlur(image,(7,7),0)

median3 = cv2.medianBlur(image,3)
median5 = cv2.medianBlur(image,5)
median7 = cv2.medianBlur(image,7)

print('image',get_blurrness_score(image))

print('blur3',get_blurrness_score(blur3))
print('Gblur3',get_blurrness_score(Gblur3))
print('median3',get_blurrness_score(median3))
print('blur5',get_blurrness_score(blur5))
print('Gblur5',get_blurrness_score(Gblur5))
print('median5',get_blurrness_score(median5))
print('blur7',get_blurrness_score(blur7))
print('Gblur7',get_blurrness_score(Gblur7))
print('median7',get_blurrness_score(median7))

cv2.imshow("image",image)
cv2.imwrite(myPath+str(get_blurrness_score(image))+'_back.jpg', image)
cv2.imwrite(myPath+str(get_blurrness_score(blur3))+'_back_blur3.jpg', blur3)
cv2.imwrite(myPath+str(get_blurrness_score(Gblur3))+'_back_Gblur3.jpg', Gblur3)
cv2.imwrite(myPath+str(get_blurrness_score(median3))+'_back_median3.jpg', median3)
cv2.imwrite(myPath+str(get_blurrness_score(blur5))+'_back_blur5.jpg', blur5)
cv2.imwrite(myPath+str(get_blurrness_score(Gblur5))+'_back_Gblur5.jpg', Gblur5)
cv2.imwrite(myPath+str(get_blurrness_score(median5))+'_back_median5.jpg', median5)
cv2.imwrite(myPath+str(get_blurrness_score(blur7))+'_back_blur7.jpg', blur7)
cv2.imwrite(myPath+str(get_blurrness_score(Gblur7))+'_back_Gblur7.jpg', Gblur7)
cv2.imwrite(myPath+str(get_blurrness_score(median7))+'_back_median7.jpg', median7)

cv2.waitKey(0)