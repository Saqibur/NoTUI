import cv2 as cv
import numpy as np
import pytesseract
import imutils
from pyimagesearch.shapedetector import ShapeDetector

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def getContoursFromFrame(frame):
    # image = cv.imread("Images/023.jfif")
    # image = cv.medianBlur(image, 3)
    image = frame
    image = cv.GaussianBlur(image, (3, 3), 0)
    result = image.copy()
    image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower = np.array([155,25,0])
    upper = np.array([179,255,255])
    mask = cv.inRange(image, lower, upper)

    _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    print(len(contours))
    for contour in contours:
        area = cv.contourArea(contour)
        print(area)
        if area > 7000.0:
            rect = cv.boundingRect(contour)
            x,y,w,h = rect
            cv.rectangle(result, (x,y), (x+w,y+h), (0,255,0), 4)
            cv.putText(result, 'Note', (x+w+10,y+h), 0, 1, (0,255,0))
            crop_img = result[y:y+h, x:x+w]
            print(pytesseract.image_to_string(crop_img))
            cv.imshow("Cropped Images", crop_img)
        cv.waitKey(500)

    # cv.drawContours(result, contours, -1, (0, 255, 0), 3)

    # result = cv.bitwise_and(result, result, mask=mask)
    return result

camera = cv.VideoCapture("Images/Video.mp4")

while True:
    check, frame = camera.read()
   
    frame = getContoursFromFrame(frame)
    cv.imshow("Frame", frame)

    key = cv.waitKey(500)
    if key == 27:
        break