import cv2 as cv
import numpy as np

# var kiritamiz
toy = np.zeros((400,400), dtype='uint8')

# To'rtburchak
rectangle = cv.rectangle(toy.copy(), (30,30), (370,370), 255, -1)

# Doira
circle = cv.circle(toy.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitli VA --> FAQAT KESISHADIGAN HUDUDLAR
b_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', b_and)

# Bitli YOKI --> KESISMAYDIGAN VA KESISHADIGAN HUDULAR
b_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', b_or)

# Bitli XOR --> FAQAT KESISMAYDIGAN HUDULAR
b_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', b_xor)

# Bitli NOT --> BOSHQA HUDUDLAR
b_not = cv.bitwise_not(rectangle, circle)
cv.imshow('Bitwise NOT', b_not)

cv.waitKey(0)