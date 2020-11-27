import numpy as np
import cv2

image = cv2.imread(r'C:\Users\Saqibur\Desktop\Projects\NoTUI\static\sample_data\colortest.jpg')
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([19,100,125])
upper = np.array([255,255,255])

mask = cv2.inRange(image, lower, upper)
result = cv2.bitwise_and(result, result, mask=mask)
print(image)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()