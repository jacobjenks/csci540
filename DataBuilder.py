import colorsys
import scipy
from PIL import Image
from matplotlib import cm
from os import listdir
import cPickle
import theano
import theano.tensor as T
import theano.sparse
import numpy
import sys


class hsvImage:
	#1D channel arrays
	hue = []
	saturation = []
	value = []
	
	def __init__(self, fileName):
		self.fileName = fileName
		
		img = Image.open(self.fileName)
		rgb = list(img.getdata())
		rows = img.size[1]
		cols = img.size[0]
		
		self.hue, self.saturation, self.value = [], [], []
		for row in range(0,rows):
			hue_row, saturation_row, value_row = [], [], []
			for col in range(0, cols):
				rgb_floats = map(lambda x: float(x) / 255, rgb[cols * row + col])
				hsv_tuple = colorsys.rgb_to_hsv(*rgb_floats)
				self.hue.append(hsv_tuple[0])
				self.saturation.append(hsv_tuple[1])
				self.value.append(hsv_tuple[2])
				#hue_row.append(hsv_tuple[0])
				#saturation_row.append(hsv_tuple[1])
				#value_row.append(hsv_tuple[2])
			#self.hue.append(hue_row)
			#self.saturation.append(saturation_row)
			#self.value.append(value_row)
			
# This combines a series of images into H, S, and V array of arrays
class ImageArray:
	hue = []
	saturation = []
	value = []
	
	def __init__(self, directory):
		imageFiles = listdir(directory)
		imagesToProcess = []
		for f in imageFiles:
			imagesToProcess.append(hsvImage(directory+"/"+f))

		for image in imagesToProcess:
			self.hue.append(image.hue)
			self.saturation.append(image.saturation)
			self.value.append(image.value)
		
#take a one dimensional array and return an rval that the autoencoder can use. This replaces load_data in logistic_sgd
def buildData(data):
	data = numpy.array(data, dtype=theano.config.floatX)
	
	shared_x = theano.shared(data, borrow=True)#convert to theano.shared for GPU processing?
	shared_y = theano.shared(numpy.zeros(len(data)), borrow=True)#Create array of empty labels
	shared_y = T.cast(shared_y, 'int32')#cast labels to ints, since float labels don't make sense
	
	# set of tuples for test_set_x, test_set_y, valid_set_x, valid_set_y, train_set_x, and train_set_y, but since this is an autoencoder these are all the same thing
	rval = [(shared_x, shared_y), (shared_x, shared_y),(shared_x, shared_y)]
	return rval
	
def buildPickle(directory):
	data = ImageArray(directory)

	f = file(directory+"/hue.pkl", 'wb')
	cPickle.dump(hue_pickle, f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()
	
	f = file(directory+"/saturation.pkl", 'wb')
	cPickle.dump(saturation_pickle, f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()
	
	f = file(directory+"/value.pkl", 'wb')
	cPickle.dump(value_pickle, f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()


def head(array):
	for i in range(0,10):
		print array[i]

if __name__ == '__main__':
	data = ImageArray("images/pickle_test_100x100")
	data = buildData(data.hue)
	#print data[0]
