import cv2 as cv
import numpy as np

# Rasm tanlaymiz
img = cv.imread('pictures/karim.jpg')
cv.imshow('BENZEMA', img)

# blank nomli o'zgaruvchi kiritamiz
blank = np.zeros((750,750,3), dtype='uint8')
# cv.imshow('Blank', blank)
#
# Fonni kulrangga o'zgartiramiz
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#
# # Xiralashtirish
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', gray)
#
# Canny
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
#
# ret, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)


contour, abc = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contour)} contour(s) found !')

cv.drawContours(blank, contour, -1, (225,234,0), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)