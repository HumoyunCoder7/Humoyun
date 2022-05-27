import cv2 as cv
import matplotlib.pyplot as mpl
# Rasm tanlaymiz
img = cv.imread('pictures/karim.jpg')
cv.imshow('BENZEMA', img)

# BGR ni RGB ga o'tkazish
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# Oddiy formula
# var = cv.cvtColor(img. cv.COLOR_...DAN2...GA)
# cv.imshow('NOMI', var)

#cv.waitKey(0)

mpl.imshow(img)
mpl.show()
