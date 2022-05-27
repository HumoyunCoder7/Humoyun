import cv2 as cv
import numpy as np

# blank nomli o'zgaruvchi kiritamiz
blank = np.zeros((1000,1000,3), dtype='uint8')
# cv.imshow('Blank', blank)
#
# ekranni bo'yash
# blank[200:300, 300:400] = 255,0,0
# cv.imshow('Blue', blank)
#
# to'rtburchak chizish
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (500,234,0), thickness=-1)
# cv.imshow('Rectangle', blank)
#
# Aylana chizish
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (345,124,765), thickness=3)
# cv.imshow('Circle', blank)
#
# Chiziq chizish
# cv.line(blank, (100,250), (300,400), (224,224,224), thickness=4)
# cv.imshow('Line', blank)
#
# Matn yozamiz
cv.putText(blank, 'Alhamdulillah', (400,400), cv.FONT_ITALIC, 1.2, (255,300,0), thickness=4)
cv.imshow('Text', blank)

cv.waitKey(0)