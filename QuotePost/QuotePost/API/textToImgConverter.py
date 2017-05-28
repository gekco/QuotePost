#TextToImageConverter
#functions - 1. convert text to image
#2. save the file and returns the name
#3. can add font, different pictures size in future

from PIL import Image, ImageDraw
import datetime
import random
from PIL import ImageFont

#default path where images will be saved
DEFAULT_IMG_PATH = "../quoteImages/"
SEPARATOR_UNDERSCORE = "_"

#default extension with which images are saved
DEFAULT_EXTENSION = '.jpg'


DEFAULT_IMG_FONT_PATH = "../image_files/"

FONT_FILE = "CHOPS___.ttf"

BG_IMGS_LEN = 6

BG_FILE_NAME = 'image'

#text color
TEXT_COL = (255,255,255)

class TextToImageConverter():
	def convertToImage(self, text,userName):
		img = self.getRandomBackground()			             #get a new background image 
		
		draw = ImageDraw.Draw(img)
		
		bg_width,bg_height = img.size							#background height and width
		
																#hardcoded font type as of now
	
		x = 10;													 #starting point
		
		drawString = ""												
		
		for word in text.split():                                #split the text into words
			text_width, text_height = draw.textsize(word)               
			if(x + text_width <= bg_width ):					 	#if fit to current line
				drawString = drawString + " " + word			#keep it in this line
				x += (text_width + 5)
			else:												 #if not fitting move to next line
				x = 10
				drawString = drawString + "\n" + word
				x += (text_width + 5)
				
		w, h = draw.textsize(drawString)						
		draw.text((10,(bg_height-h)/2), drawString, fill="white")		#render the text in the middle of image
		#img_resized = img.resize((3*bg_width,3*bg_height), Image.ANTIALIAS)			#resize the image
		
		fileName = userName + SEPARATOR_UNDERSCORE + str(datetime.datetime.now().timestamp()) + DEFAULT_EXTENSION	#save images
		img.save(DEFAULT_IMG_PATH + fileName)
		
		print("hie" + fileName)
		return DEFAULT_IMG_PATH + fileName;						#return fileName
		
	def getRandomBackground(self):
		return Image.open(DEFAULT_IMG_FONT_PATH + BG_FILE_NAME + str(random.randint(1,6)) + '.jpg')
		