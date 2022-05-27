import cv2 as cv
import numpy as np

# Rasm tanlaymiz
img = cv.imread('pictures/karim.jpg')
cv.imshow('BENZEMA', img)

# blank nomli o'zgaruvchi kiritamiz
blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)


# Average Blur
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 5)
cv.imshow('Median Blur', median)

# Bilateral
bil = cv.bilateralFilter(img, 15, 25, 35)
cv.imshow('Bilateral', bil)

cv.waitKey(0)