import cv2
import numpy as np
import face_recognition

imgUmg = face_recognition.load_image_file('data/Pan/1504.886331212461_front.jpg')
imgUmg = cv2.cvtColor(imgUmg,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('data/Pan/front.jpg')
imgTest = cv2.cvtColor(imgUmg,cv2.COLOR_BGR2RGB)

#facLoc = face_recognition.face_locations(imgUmg)[0]
#encodeUmg = face_recognition.face_encodings(imgUmg)[0]

cv2.imshow('Pan',imgUmg)
cv2.imshow('PanCard',imgTest)
cv2.waitKey(0)

print('hello')
