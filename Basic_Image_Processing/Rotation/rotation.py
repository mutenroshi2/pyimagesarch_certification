# #import the necessary libraries
import numpy as np
import argparse
import imutils
import cv2

#constructing the argument parser
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required= True, help='Path to the image')
args = vars(ap.parse_args())

#load the image and display it
image = cv2.imread(args['image'])
cv2.imshow('Original',image)

(h,w) = image.shape[:2]
(cx,cy) = (w//2,h//2)

#rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((cx, cy), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

# rotate our image by -90 degrees
M = cv2.getRotationMatrix2D((cx, cy), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

M = cv2.getRotationMatrix2D((cx - 50, cy - 50),45,1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by offset and 45 Degrees", rotated)

#imutils method
rotated = imutils.rotate(image,180)
cv2.imshow("Rotated by 180 Degrees", rotated)


cv2.waitKey(0)
cv2.destroyAllWindows()

# image = cv2.imread('wynn.png')
# cv2.imshow('image',image)
# (h,w) = image.shape[:2]
# rotation = imutils.rotate(image,-30,(w,h))
# cv2.imshow("Rotated by 180 Degrees", rotation)
#
#
# (b,g,r) = image[335,254]
# print((b,g,r))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
