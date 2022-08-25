import cv2

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
# # Load the cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# # Read the input image
# img = cv2.imread('data/Aadhar/front.jpg')
# imgResize = image_resize(img, width=600, height = 800)
# # Convert into grayscale
# gray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
#
# # Detect faces
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# print(faces)
# if faces.all():
#     print('faces present')
# else:
#     print('No face prrsent')
# # Draw rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(imgResize, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
# # Display the output
# cv2.imshow('img', imgResize)
# cv2.waitKey(0)

def face_detect(image):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if faces.all():
        return 1
    else:
        return 0

img = cv2.imread('data/Aadhar/front.jpg')
print(face_detect(img))