#import the necessary packages
import cv2
import imutils
import argparse

#construct the argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# we need to keep in mind aspect ratio so the image does not look skewed
# or distorted -- therefore, we calculate the ratio of the new image to
# the old image. Let's make our new image have a width of 150 pixels

# r = 150//image.shape[1]
# dim = (150,int(image.shape[0])*r)
#
# #perform the actual resizing of the image
# resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("Resized (Width)", resized)

resized = imutils.resize(image,width=image.shape[1]*2,inter=cv2.INTER_CUBIC)
(b,g,r) = resized[367,170]
print(b,g,r)
cv2.imshow('resized',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# construct the list of interpolation methods
# methods = [
# 	("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
# 	("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
# 	("cv2.INTER_AREA", cv2.INTER_AREA),
# 	("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
# 	("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
#
# # loop over the interpolation methods
# for (name, method) in methods:
# 	# increase the size of the image by 3x using the current interpolation
# 	# method
# 	resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
# 	cv2.imshow("Method: {}".format(name), resized)
# 	cv2.waitKey(0)

