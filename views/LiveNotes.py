from flask import render_template
from flask import render_template, redirect, url_for, request, session
from app import db
from models import Board, Note, Category
import cv2 as cv
import numpy as np
import pytesseract
import json

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
IMAGES_PATH = "static\sample_data"


def getContoursFromFrame(frame):
    # image = cv.imread("Images/023.jfif")
    # image = cv.medianBlur(image, 3)
    image = frame
    image = cv.GaussianBlur(image, (3, 3), 0)
    result = image.copy()
    image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower = np.array([10,80,120])
    upper = np.array([255,255,255])
    mask = cv.inRange(image, lower, upper)

    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    results = []
    print(len(contours))
    for contour in contours:
        area = cv.contourArea(contour)
        # print(area)
        if area > 2000.0:
            rect = cv.boundingRect(contour)
            x,y,w,h = rect
            cv.rectangle(result, (x,y), (x+w,y+h), (0,255,0), 4)
            crop_img = result[y:y+h, x:x+w]

            im_gray = cv.cvtColor(crop_img, cv.COLOR_BGR2GRAY)

            (thresh, im_bw) = cv.threshold(im_gray, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            cv.imshow("jinish", im_bw)
            label = pytesseract.image_to_string(im_bw)

            coord_dict = {"x" : f"{x}", "y" : f"{y}", "w" : f"{w}", "h" : f"{h}", "label" : f"{label}", }
            results.append(coord_dict)

    return results

def live_notes():
    notes = Note.Note.query.all()
    
    results = cv.imread(IMAGES_PATH + '/6.jpg')
    # camera = cv.VideoCapture(1)
    # _, results = camera.read()
    cats = []

    

    notes = getContoursFromFrame(results)

    for result in notes:
        if int(result["x"]) <= 80:
            cats.append(0)
        elif int(result["x"]) >= 90 and int(result["x"]) <= 400:
            cats.append(1)
        else:
            cats.append(2)

    todos  = []
    doings = []
    dones = []
    for cat in cats:
        if cat == 0:
            todos.append("todo")
        elif cat == 1:
            doings.append("doing")
        else:
            dones.append("done")

    return render_template(
            'live_notes.html',
            todos=todos,
            doings=doings,
            dones=dones,
        )