import cv2 as cv
import numpy as np

# Rasm tanlaymiz
img = cv.imread('pictures/cr7.jpg')
cv.imshow('CR7', img)

# Tarjima qilish
# def translate(img, x, y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)
#
# -x --> Chap. x --> O'ng.
# -y --> Past. y --> Tepa
# translated = translate(img, -75, 75)
# cv.imshow('Translated', translated)

# Aylantirish
def rotate(img, angle, rotPoint=None):
    (heigth,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, heigth//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.2)
    dimensions = (width, heigth)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 60)
cv.imshow('Rotated', rotated)

r_rotated = rotate(rotated, -45)
cv.imshow('R_Rotated', r_rotated)

# Aylantirish
flip = cv.flip(img, 1)
cv.imshow('Flipping', flip)


cv.waitKey(0)