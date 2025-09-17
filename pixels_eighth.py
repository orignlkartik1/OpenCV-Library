import numpy as np, cv2 as cv

img=cv.imread('Image_0.png')
assert img is not None, "file could not be read, check with os.path.exists()"

px=img[100,100] # It uses it for access the pixel value in RGB form. You only pass coordinates of those pixels.
print(px)

# for specific color pixel
blue=img[100,100,0]
print(blue)

# you can also modify pixel values in the same ways.
img[100,100]=[255,255,255]
print(img[100,100]) # Note: - It slows down numpy performance


# Now, IMAGE properties

print(img.shape) # shape functions return tuple of rows, columns and channels if colored else only first twos.

# total no. of pixels

print(img.size)

# image datatype

print(img.dtype)

