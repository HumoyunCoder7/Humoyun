import cv2 as cv
import numpy as np

# Rasm tanlaymiz
img = cv.imread('pictures/karim.jpg')
cv.imshow('BENZEMA', img)

# blank nomli o'zgaruvchi kiritamiz
blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

# O'zgaruvchilar
r,g,b = cv.split(img)

red = cv.merge([blank,blank,r])
green = cv.merge([blank,g,blank])
blue = cv.merge([b,blank,blank])

cv.imshow('RED', red)
cv.imshow('GREEN', green)
cv.imshow('BLUE', blue)

print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

# Birlashtirish
merged = cv.merge([b,g,r])
cv.imshow('Merged Image == RGB', merged)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

cv.waitKey(0)