#!/usr/bin/python

# imgtool.py: Danny Ruland
# Description: Inital image extraction and analysis tool

from PIL import Image
import os
import sys
import operator

isize = 512 #each image is 512x512 pixels - CONSTANT
box_size = 64 #32, 16 - SET BASED ON INPUT

def read_image(fname):
	try:
		fpath = os.getcwd() + "/" + fname
		img = Image.open(fpath)
		return img
	except:
		return None


def split_image(img, fname):
	'''
	Splits an input image into individual fragments based on
	box_size and saves them as individual files in a directory	
	'''
	try:
		os.mkdir(fname[:-4])
	except:
		pass
		
	fpath = os.getcwd() + '/' + fname[:-4] + '/'
	
	for i in range(isize/box_size):
		for j in range(isize/box_size):
			x0 = i * box_size
			x1 = x0 + box_size
			y0 = j * box_size
			y1 = y0 + box_size
			
			img_i = img.crop((x0, y0, x1, y1))
			img_name = fpath + str(i) + '-' + str(j) + '.png'
			img_i.save(img_name)
			img_i.close()
		


def image_splitter():
	fname = sys.argv[1]
	if len(fname) == 0:
		print "No filename given"
		sys.exit(0)
	
	img = read_image(fname)
	if img != None:
		img.show()
	else:
		print "Error opening file: %s" % fname
		sys.exit(0)
	
	split_image(img, fname)
	img.close()


# debug driver
if __name__=='__main__':
	image_splitter()
	
