
import numpy as np
# import pandas as pd
import cv2
import pytesseract
from dewarpper import dewarp_book
# from sign_detect import extract_signature
import mediapipe as mp
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
def get_blurrness_score(image):
    # image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(image, cv2.CV_64F).var()
    return fm


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

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\mangl\\Tesseract-OCR\\tesseract.exe'
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
                # cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 3)
                # cv2.putText(img, b[11], (x, y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 250), 2)
                # print(b[11])
                text.append(b[11])

    # cv2.imshow("result",img)
    x = filter(text)
    # print(text)
    return x


def filter(text):
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


def face_detection(image):
    mpFaceDetection = mp.solutions.face_detection
    mpDraw = mp.solutions.drawing_utils
    faceDetection = mpFaceDetection.FaceDetection()

    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            return detection.score


# def final_score(image):
#     img = cv2.imread(image)
#
#     # img = cv2.resize(img, (800, 200))
#     # img = dewarp_book(img)
#     print(list(img.shape))
#     score = {"blur": get_blurrness_score(img), "uniformity": average_pixel_width(img),
#              "sharpness": sharpness_score(img), "text": ExtractText(img), "Face": face_detection(img)}
#     # cv2.imshow('Image', img)
#     #
#     #
#     # print("_____")
#     # face_detection(im)
#     # print("///
#
#     text = ExtractText(img)
#     print(text)
#     if len(text) == 4:
#         score['text_score'] = 100
#     else:
#         score['text_score'] = 0
#     #
#     return score
    # new_img = dewarp_book(img)
    # new_img = cv2.resize(new_img, (1280, 720))
    #
    # cv2.imshow("cropped.jpg", img)
    # # new_img = cv2.resize(new_img, (1280, 720))
    # # new_img = extract_signature(new_img)
    # # cv2.imshow("Output", new_img)
    # cv2.waitKey(0)
#
# final_score('C:/Users/mangl/PycharmProjects/djangouploads/images/front2.jpg')
image = cv2.imread('data/Aadhar/front.jpg')
img = image_resize(image, width=600, height = 800)
img1 = dewarp_book(img)
# score = {"blur": get_blurrness_score(img1), "uniformity": average_pixel_width(img1),
#              "sharpness": sharpness_score(img1), "text": ExtractText(img1), "Face": face_detection(img1)}
print(face_detection(img1))

cv2.imshow("Blank", img)
cv2.imshow("Blank1", img1)

cv2.waitKey(0)