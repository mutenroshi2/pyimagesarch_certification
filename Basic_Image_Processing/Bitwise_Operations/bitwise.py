#import libraries
import cv2
import numpy as np

#first draw a rectangle
rectangle = np.zeros((300,300),dtype='uint8')
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("Rectangle", rectangle)

#draw a circle
circle = np.zeros((300,300),dtype='uint8')
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow('Circle',circle)

# A bitwise 'AND' is only True when both rectangle dand circle have
# a value that is 'ON.' Simply put, the bitwise AND function
# examines every pixel in rectangle and circle. If both pixels
# have a value greater than zero, that pixel is turne 'ON' (i.e
# set to 255 in the output image). If both pixels are not greater
# than zero, then the output pixel is left 'OFF' with a value of 0.
bitwiseand = cv2.bitwise_and(rectangle,circle)
bitwiseor = cv2.bitwise_or(rectangle,circle)
bitwisexor = cv2.bitwise_xor(rectangle,circle)
bitwiseanot = cv2.bitwise_not(circle)

cv2.imshow('AND',bitwiseand)
cv2.imshow('OR',bitwiseor)
cv2.imshow('XOR',bitwisexor)
cv2.imshow('NOT',bitwiseanot)
cv2.waitKey(0)
cv2.destroyAllWindows()