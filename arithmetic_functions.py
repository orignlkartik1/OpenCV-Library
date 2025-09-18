import cv2 as cv
import numpy as np

# Read two images (ensure they are the same size)
img1 = cv.imread('image_0.png')
img2 = cv.imread('image_1.png')

img=cv.imread('added_image.jpg')
# Resize if needed to match dimensions
img1 = cv.resize(img1, (500, 500))
img2 = cv.resize(img2, (500, 500))

# Perform saturated addition
#result = cv.add(img1, img2)

# Save or display result
#cv.imwrite('added_image.jpg', result)
#cv.imshow("new image",img)
dst = cv.addWeighted(img1,0.3,img2,0.9,0)

cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()