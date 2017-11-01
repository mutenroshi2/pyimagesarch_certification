#import required libraries
import cv2
import argparse
import imutils

#make the required argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help='Path to the image')
args = vars(ap.parse_args())

#load the image and display it
image = cv2.imread(args["image"])
cv2.imshow('Original',image)

#flip the image horizontally
h_flipped = cv2.flip(image,1)
rotate = imutils.rotate(h_flipped,45)
v = cv2.flip(rotate,0)
[b,g,r] = v[189,441]
print([b,g,r])
cv2.imshow('Horizontal',h_flipped)

#flip the image vertically
v_flipped = cv2.flip(image,0)
cv2.imshow('Vertical',v_flipped)

#flip the image vertically and horizontally
vh_flipped = cv2.flip(image,-1)
cv2.imshow('Horizontal and vertical',vh_flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()