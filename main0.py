import cv2 as cv

img = cv.imread('pictures/cr7.jpg')

cv.imshow('CR7', img)

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width, heigth)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def changeRes(width, heigth):
    capture.set(3,width)
    capture.set(4,heigth)

resized_image = rescaleFrame(img)
cv.imshow("Image", resized_image)

capture = cv.VideoCapture('videos/cr7.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.5)

    cv.imshow('Video', frame)

    cv.imshow('CR7', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
capture.destroyAllWindows()



