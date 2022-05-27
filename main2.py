import cv2 as cv

# Rasm tanlaymiz
img = cv.imread('pictures/cr7.jpg')
cv.imshow('CR7', img)

# To'q kulrang rangga o'tkazish
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Xiralashtirish
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Chetki kaskad
# canny = cv.Canny(img, 125, 125)
# cv.imshow('Canny', canny)

# Tasvirni kengaytirish
# dilated = cv.dilate(img, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# Yaradorlash
# eroded = cv.erode(img, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# Hajmni o'zgartirish
# resize = cv.resize(img, (750,750), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resize', resize)
#
# Kesish
cropped = img[200:400, 200:400]
cv.imshow('Cropping', cropped)


cv.waitKey(0)