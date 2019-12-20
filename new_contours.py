import cv2 as cv
import numpy as np

image = cv.imread("Images/023.jfif")
# image = cv.medianBlur(image, 3)
image = cv.GaussianBlur(image, (3, 3), 0)
result = image.copy()
image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
lower = np.array([155,25,0])
upper = np.array([179,255,255])
mask = cv.inRange(image, lower, upper)

_, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print(len(contours))

for contour in contours:
    rect = cv.boundingRect(contour)
    x,y,w,h = rect
    cv.rectangle(result, (x,y), (x+w,y+h), (0,255,0), 4)
    cv.putText(result, 'Note', (x+w+10,y+h), 0, 1, (0,255,0))
    area = cv.contourArea(contour)
    print(area)

# cv.drawContours(result, contours, -1, (0, 255, 0), 3)

# result = cv.bitwise_and(result, result, mask=mask)

cv.imshow('mask', mask)
cv.imshow('result', result)
cv.waitKey(0)