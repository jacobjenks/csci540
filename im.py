import colorsys
import numpy as num
import scipy
from PIL import Image
from matplotlib import cm
from os import listdir

class hsvImage:
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
				hue_row.append(hsv_tuple[0])
				saturation_row.append(hsv_tuple[1])
				value_row.append(hsv_tuple[2])
			self.hue.append(hue_row)
			self.saturation.append(saturation_row)
			self.value.append(value_row)
		
	
def buildPickle(dir)
	imageFiles = listdir("images/pickle_test_100x100")
	imagesToProcess = []
	for file in imageFiles:
		imagesToProcess.append(hsvImage(file))

	hue_pickle = []
	sat_pickle = []
	value_pickle = []

#autoencode here


rgb_processed = []
for row in range(0,rows):
    for col in range(0, cols):
        h, s, v = tuple(map(lambda y: y[row][col], (hue, saturation, value)))
        rgb_ints = tuple(map(lambda x: int(x*255), colorsys.hsv_to_rgb(h, s,v)))
        rgb_processed.append(rgb_ints)

img_out = Image.new(img.mode, img.size)
img_out.putdata(rgb_processed)
img_out.save("out.bmp")


