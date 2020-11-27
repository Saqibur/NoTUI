import sys
import numpy as np
import cv2 as cv
import pytesseract
import imutils
from pyimagesearch.shapedetector import ShapeDetector


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def denoiseGaussian(image):
    return cv.GaussianBlur(image, (3, 3), 0)

def denoiseBilateral(image):
    return cv.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

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

def isolate_red(image):
    result = image.copy()
    image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower_red = np.array([155,25,0])
    upper_red = np.array([179,255,255])
    mask = cv.inRange(image, lower_red, upper_red)
    result = cv.bitwise_and(result, result, mask=mask)
    return result

def ocr_core(image):
    text = pytesseract.image_to_string(image)
    return text

def shapes(image):
    thresh = cv.threshold(image, 60, 255, cv.THRESH_BINARY)[1]
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])
    # find contours in the thresholded image and initialize the
    # shape detector
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()
    # loop over the contours
    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv.moments(c)
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)
    
        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        print(c)
        cv.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv.putText(image, shape, (cX, cY), cv.FONT_HERSHEY_SIMPLEX,
            0.5, (255, 255, 255), 2)
    
        # show the output image
        cv.imshow("Image", image)
        cv.waitKey(0)

def drawPoints(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # print(contours)
    
    # cv.drawContours(image, contours, -1, (0,255,0), 3)

    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
	        cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    cnt = contours[0]
    x,y,w,h = cv.boundingRect(cnt)
    image = cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow("magic", image)
    cv.waitKey(0)

# So far getting the best results with the bilateral filter.

# test_image = cv.imread('Images/014.jfif')
# cv.imshow("Original", test_image)
# cv.imshow("Gaussian", denoiseGaussian(test_image))
# cv.imshow("Bilateral", denoiseBilateral(test_image))
# cv.imshow("Laplacian on Original", applyLaplacianFilter(test_image))
# cv.imshow("Laplacian on Bilateral", applyLaplacianFilter(denoiseBilateral(test_image)))
# cv.imshow("Laplacian on Gaussian", applyLaplacianFilter(denoiseGaussian(test_image)))
# cv.waitKey(0)

test_image = cv.imread('Images/023.jfif')
# cv.imshow("Original", test_image)
# cv.imshow("Red removed", isolate_red(test_image))
# print(ocr_core(isolate_red(test_image)))
# cv.imshow("Laplacian on Original", applyLaplacianFilter(denoiseBilateral(isolate_red(test_image))))
print(ocr_core(isolate_red(test_image)))
# test_image = cv.imread('Images/023.jfif')
drawPoints(denoiseBilateral(isolate_red(test_image)))
cv.waitKey(0)