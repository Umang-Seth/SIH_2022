import cv2
import numpy as np

def empty(a):
    pass

def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    #print("diff",diff)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    #print(myPointsNew)
    return myPointsNew


def getWarp(img, reorder):
    pts1 = np.float32(reorder)
    pts2 = np.float32([[0, 0], [Width, 0], [0, Height], [Width, Height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (Width, Height))
    return imgOutput

point_matrix = np.zeros((4, 2),int)
counter = 0


def mousePoints(event, x, y, flags, params):
    global counter
    # Left button mouse click event <a href="https://thinkinfi.com/basic-python-opencv-tutorial-function/" data-internallinksmanager029f6b8e52c="14" title="OpenCV" target="_blank" rel="noopener">opencv</a>
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix[counter] = x, y
        counter = counter + 1



Width = 480
Height = 640
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
#cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
#cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
#cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
#cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
#cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",0,255,empty)

img = cv2.imread('12.jpeg')
imgr = cv2.resize(img, (480,640), interpolation=cv2.INTER_AREA)

while True:
    for x in range(0, 4):
        cv2.circle(imgr, (point_matrix[x][0], point_matrix[x][1]), 3, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Original Image ", imgr)
    # Mouse click event on original image
    cv2.setMouseCallback("Original Image ", mousePoints)
    reord = reorder(point_matrix)

    imgOutput = getWarp(imgr,reord)
    cv2.imshow("Warp",imgOutput)
    ones = np.ones(imgOutput.shape, dtype="uint8")*50
    imgBright = cv2.add(imgOutput, ones)
    cv2.imshow('Bright', imgBright)

    # print(point_matrix)
    # Refreshing window all time



    cv2.waitKey(1)
