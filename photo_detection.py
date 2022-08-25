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


image = cv2.imread('data/Pan/front2.jpg')
img = image_resize(image, width=600, height = 800)
imgCrop = img[400:650,50:450]
#imgCrop = img[200:650,150:450]
cv2.rectangle(img, (50, 400), (450, 650), (255, 0, 255), 2)

# mpFaceDetection = mp.solutions.face_detection
# mpDraw = mp.solutions.drawing_utils
# faceDetection = mpFaceDetection.FaceDetection()
#
# imgRGB = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2RGB)
# results = faceDetection.process(imgRGB)
#print('results',results)

def face_detection(image):
    mpFaceDetection = mp.solutions.face_detection
    mpDraw = mp.solutions.drawing_utils
    faceDetection = mpFaceDetection.FaceDetection()

    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id,detection in enumerate(results.detections):
            return detection.score
        # print(detection.location_data.relative_bounding_box)
        # bboxC = detection.location_data.relative_bounding_box
        # ih, iw, ic = imgCrop.shape
        # bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
        #        int(bboxC.width * iw), int(bboxC.height * ih),
        # cv2.rectangle(imgCrop,bbox,(255,0,255),2)

cv2.imshow('Image', img)
cv2.imshow('Crop',imgCrop)
print('Score',face_detection(imgCrop))
cv2.waitKey(0)