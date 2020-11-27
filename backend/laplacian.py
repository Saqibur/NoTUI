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