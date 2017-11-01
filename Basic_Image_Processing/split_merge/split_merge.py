#import the libraries
import cv2
import argparse
import numpy as np

#construct the argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i',"--image",required=True,help='Path to the image')
args = vars(ap.parse_args())

#load the image
image = cv2.imread(args["image"])
(B,G,R) = cv2.split(image)
print(G[5,80])
# [x,y] = R[180,94]
# print([x,y])
#show each channel individually
cv2.imshow('Red',R)
cv2.imshow('Green',G)
cv2.imshow('Blue',B)
cv2.waitKey(0)


# merge the image back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# visualize each channel in color
zeros = np.zeros(image.shape[:2],dtype='uint8')
cv2.imshow('Red',cv2.merge([zeros,zeros,R]))
cv2.imshow('Green',cv2.merge([zeros,G,zeros]))
cv2.imshow('Blue',cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)




