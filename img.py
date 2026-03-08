import cv2 as cv

#Reading images

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)