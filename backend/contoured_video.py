import cv2 as cv
import numpy as np
import pytesseract
import json

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'

def applyLaplacianFilter(image, kernel_size=3):
    '''
        Returns the the input image after applying the laplacian filter to it.
        Loads an image
        Remove noise by applying a Gaussian blur and then convert the original image to grayscale
        Applies a Laplacian operator to the grayscale image and stores the output image
        Display the result in a window

        ddepth: Depth of the destination image. Since our input is CV_8U we define ddepth = CV_16S to avoid overflow
        kernel_size: The kernel size of the Sobel operator to be applied internally. We use 3 in this example.

    '''
    
    ddepth = cv.CV_16S
    # window_name = "Laplacian Applied"

    # imageName = "helpme.jfif"
    # src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)
    
    # src = cv.resize(image, None, fx=0.4, fy=0.4)

    src_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # cv.namedWindow(window_name)

    dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
    
    abs_dst = cv.convertScaleAbs(dst)
    
    # cv.imshow(window_name, abs_dst)
    # cv.waitKey(0)
    return abs_dst

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
            lol = applyLaplacianFilter(crop_img)
            (thresh, im_bw) = cv.threshold(im_gray, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            cv.imshow("jinish", im_bw)
            label = pytesseract.image_to_string(im_bw)

            
            coord_dict = {"x" : f"{x}", "y" : f"{y}", "w" : f"{w}", "h" : f"{h}", "label" : f"{label}", }
            with open("data_file.json", "w") as write_file:
                json.dump(coord_dict, write_file)

            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(result, label, (x+w+10,y+h), fontFace=font, fontScale=0.5, color=(255,0,0), thickness=2)
            # cv.waitKey(1000)
            cv.imshow("lol", lol)

    # cv.drawContours(result, contours, -1, (0, 255, 0), 3)

    # result = cv.bitwise_and(result, result, mask=mask)
    return result

# camera = cv.VideoCapture(0)
while True:
    
    frame = getContoursFromFrame(cv.imread(r'C:\Users\Saqibur\Desktop\Projects\NoTUI\static\sample_data\4.jpg'))
    cv.imshow("Frame", frame)
    cv.waitKey(0)
    exit()