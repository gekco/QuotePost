#TextToImageConverter
#functions - 1. convert text to image
#2. save the file and returns the name
#3. can add font, different pictures size in future

from PIL import Image, ImageDraw
import datetime
import random
from PIL import ImageFont
from os import listdir
import os.path

#default path where images will be saved
DEFAULT_IMG_PATH = "../quoteImages/"

SEPARATOR_UNDERSCORE = "_"

#default extension with which images are saved
DEFAULT_EXTENSION = '.jpg'

#default path where background images are present
DEFAULT_BG_IMG_PATH = "../bgImageFiles/"

#count of images in folder where background images are present
BG_IMGS_LEN = len(listdir(DEFAULT_BG_IMG_PATH))

#prefix of file in BG_FILE_FOLDER
BG_FILE_NAME = 'image'

#horizontal x coordinate where we will start rendering text
START_X = 10

#text color
TEXT_COL = (255,255,255)

class TextToImageConverter():
	def convertToImage(self, text,userName):
		img = self.getRandomBackground()			             		#get a new background image 
		
		draw = ImageDraw.Draw(img)
		
		bg_width,bg_height = img.size									#background height and width
																
		drawString = self.getStringAccToPicture(text, draw, bg_width)	#get multiline String As It will fit inside the picture. 												
				
		w, h = draw.textsize(drawString)						
		draw.text((START_X,(bg_height-h)/2), drawString, fill="white")		#render the text in the middle of image
		
		fileName = userName + SEPARATOR_UNDERSCORE + str(datetime.datetime.now().timestamp()) + DEFAULT_EXTENSION	#save images
		img.save(DEFAULT_IMG_PATH + fileName)
		return DEFAULT_IMG_PATH + fileName;						#return fileName
		
		#the bg files are stored in a format 'image1.jpg' 'image2.jpg' and so on. we find the random image from these
	def getRandomBackground(self):
		for i in range(0, 10):																#check if file exists for any 10 random integers
			ri = random.randint(1,BG_IMGS_LEN)
			if(os.path.isfile(DEFAULT_BG_IMG_PATH + BG_FILE_NAME + str(ri) + '.jpg')):
				return Image.open(DEFAULT_BG_IMG_PATH + BG_FILE_NAME + str(ri) + '.jpg')
		return Image.new("RGBA", (200,200),(120,20,20))										#return deafult image if not found
	
	def getStringAccToPicture(self,text,draw,bg_width):
		x = START_X
		drawString =""
		for word in text.split():                                #split the text into words
			text_width, text_height = draw.textsize(word)               
			if(x + text_width <= bg_width ):					 	#if fit to current line
				drawString = drawString + " " + word			#keep it in this line
				x += (text_width + 5)
			else:												 #if not fitting move to next line
				x = 10
				drawString = drawString + "\n" + word
				x += (text_width + 5)
		return drawString