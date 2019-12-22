import numpy as np
import cv2

image = cv2.imread('Images/table.jfif')
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0,0,0])
upper = np.array([50,50,100])
mask = cv2.inRange(image, lower, upper)
result = cv2.bitwise_and(result, result, mask=mask)

cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()