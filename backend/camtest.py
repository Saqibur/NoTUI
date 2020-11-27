import cv2 as cv
camera = cv.VideoCapture(1)
_, results = camera.read()
cv.imshow("nope", results)
cv.waitKey(0)
exit()