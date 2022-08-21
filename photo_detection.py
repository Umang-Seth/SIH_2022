# import cv2
# import numpy as np
# import face_recognition
#
# def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
#     # initialize the dimensions of the image to be resized and
#     # grab the image size
#     dim = None
#     (h, w) = image.shape[:2]
#
#     # if both the width and height are None, then return the
#     # original image
#     if width is None and height is None:
#         return image
#
#     # check to see if the width is None
#     if width is None:
#         # calculate the ratio of the height and construct the
#         # dimensions
#         r = height / float(h)
#         dim = (int(w * r), height)
#
#     # otherwise, the height is None
#     else:
#         # calculate the ratio of the width and construct the
#         # dimensions
#         r = width / float(w)
#         dim = (width, int(h * r))
#
#     # resize the image
#     resized = cv2.resize(image, dim, interpolation = inter)
#
#     # return the resized image
#     return resized
#
# img = cv2.imread('umang.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# imgT = cv2.imread('data/Voter/front.jpg')
# imgT = cv2.cvtColor(imgT, cv2.COLOR_BGR2RGB)
#
# imgElon = image_resize(img, width=600, height = 800)
# imgTest = image_resize(imgT, width=600, height = 800)
#
# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
#
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
#
# results = face_recognition.compare_faces([encodeElon], encodeTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeTest)
# print(results, faceDis)
# cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
#
# cv2.imshow('Elon Musk', imgElon)
# cv2.imshow('Elon Test', imgTest)
# cv2.waitKey(0)

import cv2
import mediapipe as mp
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


image = cv2.imread('data/Voter/front.jpg')
img = image_resize(image, width=600, height = 800)
imgCrop = img[200:650,150:450]
#cv2.rectangle(img, (150, 200), (450, 650), (255, 0, 255), 2)


mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

imgRGB = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2RGB)
results = faceDetection.process(imgRGB)
print(results)

if results.detections:
    for id,detection in enumerate(results.detections):
        print(detection.score)
        print(detection.location_data.relative_bounding_box)
        bboxC = detection.location_data.relative_bounding_box
        ih, iw, ic = imgCrop.shape
        bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
               int(bboxC.width * iw), int(bboxC.height * ih),
        cv2.rectangle(imgCrop,bbox,(255,0,255),2)

cv2.imshow('Image', img)
cv2.imshow('Crop',imgCrop)

cv2.waitKey(0)