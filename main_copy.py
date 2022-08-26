import re

import numpy as np
# import pandas as pd
import cv2
import pytesseract
import mediapipe as mp
from dewarpper import dewarp_book
#from sign_detect import extract_signature


def get_blurrness_score(image):
    # image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(image, cv2.CV_64F).var()
    if fm > 100:
        return 1
    else:
        return 0


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


# def centroid(img):
#     gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret, thresh = cv2.threshold(gray_image, 127, 255, 0)
#     M = cv2.moments(thresh)
#     cX = int(M["m10"] / M["m00"])
#     cY = int(M["m01"] / M["m00"])
#     return [cX, cY]


def ExtractText(img):
    # Import required packages

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    text = []
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    himg, wimg, _ = img.shape
    boxes = pytesseract.image_to_data(gray)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            # print(b)
            b = b.split()
            # print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 3)
                cv2.putText(img, b[11], (x, y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 250), 2)
                #print(b[11])
                text.append(b[11])

    #cv2.imshow("result",img)
    x = filterAadhar(text)
    #print(text)
    return x

def face_detect(image):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if faces.all():
        return 1
    else:
        return 0



def filterPan(text):

    temp = []
    new_text = {}
    name_count = 0
    for i in text:
        if (str.isupper(i[0]) is True) and len(i) > 2:
            temp.append(i)

    for i in range(0, len(temp) - 1):
        if temp[i] == 'Card':
            new_text["Card Number"] = temp[i + 1]

        elif temp[i] == 'Name' and name_count == 0:
            if str.isupper(temp[i + 1]) is True:
                new_text["Name"] = temp[i + 1] + " " + temp[i + 2]
            name_count = 1

        elif temp[i] == 'Name':
            if str.isupper(temp[i + 1]) is True and str.isupper(temp[i + 2]) is True and str.isupper(
                    temp[i + 3]) is True:
                new_text["Father's Name"] = temp[i + 1] + " " + temp[i + 2] + " " + temp[i + 3]

            else:
                new_text["Father's Name"] = temp[i + 1] + " " + temp[i + 2]

        else:
            pass

    if "Birth" in text:
        new_text["DOB"] = text[text.index("Birth") + 1]
    else:
        pass

    return new_text
    # print(new_text)


def filterAadhar(text):

    temp = []
    new_text = {}
    number = []
    # name_count = 0
    for i in text:
        if (str.isupper(i[0]) is True) and len(i) > 2:
            temp.append(i)
    #print(temp)
    # for i in range(0, len(temp) - 1):
    #
    #     if temp[i] == 'Name' and name_count == 0:
    #         if str.isupper(temp[i + 1]) is True:
    new_text["Name"] = str(temp[0] + " " + temp[1])
            # name_count = 1

        # elif temp[i] == 'Name':
        #     if str.isupper(temp[i + 1]) is True and str.isupper(temp[i + 2]) is True and str.isupper(
        #             temp[i + 3]) is True:
        #         new_text["Father's Name"] = temp[i + 1] + " " + temp[i + 2] + " " + temp[i + 3]
        #
        #     else:
        #         new_text["Father's Name"] = temp[i + 1] + " " + temp[i + 2]

        # else:
        #     pass

    for i in range(0,len(text)):
        #print(text[i].find("MALE"))
        if text[i].find("DOB") >= 0:
            new_text["DOB"] = text[i+ 1]
        elif text[i].find("MALE") >= 0 or text[i].find("FEMALE") >= 0:
            new_text["GENDER"] = text[i]
        elif text[i].find("Mobile") >= 0:
            new_text["MOBILE"] = text[i+2]
        elif text[i].isnumeric():
            if len(text[i])==4:
                number.append(text[i])
        else:
            pass
    new_text["AADHAR"] = str(number[0] + " " + number[1] + " " + number[2])
    #print(number)
    return new_text
    # print(new_text)



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

def final_score(image):
    img = cv2.imread(image)

    #im = cv2.resize(img, (800, 200))
    im = image_resize(img, width=600, height = 800)

    # im = dewarp_book(im)
    score = {"blur": get_blurrness_score(img), "uniformity": average_pixel_width(img),
             "sharpness": sharpness_score(img), "text": ExtractText(im),"face":face_detect(img)}


    text = ExtractText(img)
    if len(text) == 5:
        score['text_score'] = 100
    else:
        score['text_score'] = 0

    avg = (((score['blur'] * 100) + (score['uniformity']) + (score['text_score']) + (score['face'] * 100)) / 4)
    #print(avg)
    #print(score)
    return avg
    #
    # cv2.imshow("Output", img)
    # cv2.waitKey(0)
    # return score
    # new_img = dewarp_book(img)
    # new_img = cv2.resize(new_img, (1280, 720))
    #
    # cv2.imshow("cropped.jpg", img)
    # # new_img = cv2.resize(new_img, (1280, 720))
    # # new_img = extract_signature(new_img)
    # # cv2.imshow("Output", new_img)
    # cv2.waitKey(0)



final_score('data/Aadhar/shivam.jpg')
# img = cv2.imread('data/Aadhar/shivam.jpg')
# imgResize = image_resize(img, width=600, height = 800)
# cv2.imshow('Image',imgResize)
# text = ExtractText(imgResize)
# #print(text)
# cv2.imshow('Image Resize',imgResize)
#
# cv2.waitKey(0)
