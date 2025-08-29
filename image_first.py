# Import Libraries or Setup environment
import cv2 as cv
import sys

# read an image file
img=cv.imread("Image_0.png",cv.IMREAD_GRAYSCALE) # In the second argument, I'm changing the color of image. By default, It is IMAGE_COLOR BGR (8-BIT format). You can use other formats.

# by using sys module if output is none, it stops the program
if img is None:
    sys.exit("Image is not Available.")

# Display a window of your image
cv.imshow("Display Window",img)

# This use for img waits until any key is not press.
k=cv.waitKey(0)

# if key pressed is small case letter of 's,' then it saves your image in cwd.
if k==ord("s"):

    # this use for saving file in your current working directory.
    cv.imwrite("choose_file.png",img)