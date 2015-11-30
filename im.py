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
		
		self.__img = Image.open(self.fileName)
		rgb = list(self.__img.getdata())
		self.__rows = self.__img.size[1]
		self.__cols = self.__img.size[0]
		
		self.hue, self.saturation, self.value = [], [], []
		for row in range(0,self.__rows):
			hue_row, saturation_row, value_row = [], [], []
			for col in range(0, self.__cols):
				rgb_floats = map(lambda x: float(x) / 255, rgb[self.__cols * row + col])
				hsv_tuple = colorsys.rgb_to_hsv(*rgb_floats)
				hue_row.append(hsv_tuple[0])
				saturation_row.append(hsv_tuple[1])
				value_row.append(hsv_tuple[2])
			self.hue.append(hue_row)
			self.saturation.append(saturation_row)
			self.value.append(value_row)

        def output_image(self, output_file):
            rgb_processed = []
            for row in range(0,self.__rows):
                for col in range(0, self.__cols):
                    h, s, v = tuple(map(lambda y: y[row][col], (self.hue, self.saturation, self.value)))
                    rgb_ints = tuple(map(lambda x: int(x*255), colorsys.hsv_to_rgb(h, s,v)))
                    rgb_processed.append(rgb_ints)
            
            img_out = Image.new(self.__img.mode, self.__img.size)
            img_out.putdata(rgb_processed)
            img_out.save(output_file)
		            
	
def buildPickle(dir):
	imageFiles = listdir("images/pickle_test_100x100")
	imagesToProcess = []
	for file in imageFiles:
		imagesToProcess.append(hsvImage(file))

	hue_pickle = []
	sat_pickle = []
	value_pickle = []

if __name__ == '__main__':
    test = hsvImage("test.jpg")
    test.output_image("test_out.bmp")
