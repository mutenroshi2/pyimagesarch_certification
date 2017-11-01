# import the required libraries
import cv2

class RGBHistogram:
	def __init__(self, bins):
		# store the number of bins the histogram will use
		self.bins = bins

	def describe(self, image, mask=None):
		# compute a 3D histogram in the RGB colorspace then normalize the histogram so
		# that images with the same content
		"""
		cv2.calcHist([image array],[List of the dims channels used to compute the histogram],optional mask,
		[Array of histogram sizes in each dimension],[Array of the dims arrays of the histogram bin
		boundaries in each dimension])

		cv2.normalize(input array, output arary)
		"""
		hist = cv2.calcHist([image], [0, 1, 2],
			mask, self.bins, [0, 256, 0, 256, 0, 256])
		cv2.normalize(hist, hist) #Normalizes the value range of an array

		# return out 3D histogram as a flattened array
		return hist.flatten()