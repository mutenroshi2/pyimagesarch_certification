# import the required libraries
from imutils import paths
import numpy as np
import argparse
import cv2
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
import rgbhistogram
from rgbhistogram import RGBHistogram

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--images",required=True,help="Path to the image dataset")
ap.add_argument("-m","--masks", required=True,help="Path to image masks")
args = vars(ap.parse_args())

# Get the image and mask path
image_path = sorted(list(paths.list_images(args["images"])))
mask_path = sorted(list(paths.list_images(args["masks"])))
# print(image_path)

# create data and target arrays
data = []
target = []

# initialize the image descriptor/provide the bins for the histogram
desc = RGBHistogram([8, 8, 8])

#looop over the image and mask paths
for(image_add,mask_add) in zip(image_path,mask_path):
    #load the image and mask
    image = cv2.imread(image_add)
    mask = cv2.imread(mask_add)
    mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)

    # Image description and Image histogram
    """
    Returns the 3D histogram in the RGB colorspace then normalize the histogram and flatten the data from a 3D histogram
    to a 1D array
    """
    features = desc.describe(image,mask)

    # add the features to the data
    data.append(features)
    target.append(image_add.split("_")[-2])

# Grab the target names and encode the lables
target_names = np.unique(target)
lable_encode = LabelEncoder()
target = lable_encode.fit_transform(target)

# constructing the training data to be 70% of the data and testing to be 30%
"""
train_test_split(*arrays,test_size: % of data to be used for testing the model,random_state: generates a random number)
"""
(train_data,test_data,train_target,test_target) = train_test_split(data,target,test_size=0.3,random_state=42)

#train the classifier with 25 decession trees
model = RandomForestClassifier(n_estimators=25,random_state=85)
model.fit(train_data,train_target)

# evaluate the classifier
print(classification_report(test_target,model.predict(test_data),target_names=target_names))

#loop over a 'n' number of images
for i in np.random.choice(np.arange(0,len(image_path)),10):
    # get image and mask paths
    imagepath = image_path[i]
    maskpath = mask_path[i]

    # load the image and mask
    image = cv2.imread(imagepath)
    mask = cv2.imread(maskpath)
    mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)

    # Image description and Image histogram
    features = desc.describe(image,mask)

    #predict what the flower is
    flower = lable_encode.inverse_transform(model.predict(features.reshape(1,-1)))[0]
    print("[INFO] prediction: {}, path: {}".format(flower.upper(), imagepath))
    cv2.imshow("image", image)
    cv2.waitKey(0)