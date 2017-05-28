from PIL import Image, ImageDraw
import datetime

DEFAULT_IMG_PATH = "../quoteImages/"
SEPARATOR_UNDERSCORE = "_"
DEFAULT_EXTENSION = '.png'

class TextToImageConverter():
	def convertToImage(self, text,userName):
		print("HELLO")
		img = Image.new('RGB', (200, 100), (255, 255, 255))
		d = ImageDraw.Draw(img)
		d.text((20, 20),text, fill=(255, 0, 0))
		
		fileName = userName + SEPARATOR_UNDERSCORE + str(datetime.datetime.now().timestamp()) + DEFAULT_EXTENSION
		img.save(DEFAULT_IMG_PATH + fileName)
		
		return DEFAULT_IMG_PATH + fileName;
		
	