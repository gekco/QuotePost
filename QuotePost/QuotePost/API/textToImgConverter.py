#TextToImageConverter
#functions - 1. convert text to image
#2. save the file and returns the name
#3. can add font, different pictures size in future

from PIL import Image, ImageDraw
import datetime

#default path where images will be saved
DEFAULT_IMG_PATH = "../quoteImages/"
SEPARATOR_UNDERSCORE = "_"
#default extension with which images are saved
DEFAULT_EXTENSION = '.png'

#width of image
IMG_WIDTH = 200

#height of image
IMG_HEIGHT = 200
IMG_SIZE = (IMG_HEIGHT,IMG_WIDTH)
#image background color
IMG_BG_COL = (0,0,0)
#text color
TEXT_COL = (255,0,0)

class TextToImageConverter():
	def convertToImage(self, text,userName):
		img = Image.new('RGB', IMG_SIZE, IMG_BG_COL)             #get a new image 
		d = ImageDraw.Draw(img) 
		
		x = 10;													 #starting point
		y = 10;
		
		for word in text.split():                                #split the text into words
			text_width, text_height = d.textsize(word)               
			if(x + text_width <= IMG_WIDTH ):					 #if fit to current line
				d.text((x, y),word, fill=TEXT_COL)
				x += (text_width + 5)
			else:												 #if not fitting move to next line
				x = 10
				y += text_height + 5
				d.text((x,y),word, fill = TEXT_COL)
				x += (text_width + 5)
		
		fileName = userName + SEPARATOR_UNDERSCORE + str(datetime.datetime.now().timestamp()) + DEFAULT_EXTENSION
		img.save(DEFAULT_IMG_PATH + fileName)
		
		return DEFAULT_IMG_PATH + fileName;						#return fileName
		
	