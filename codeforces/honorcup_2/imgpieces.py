#!/usr/bin/python

# imgpieces.py: Danny Ruland
# Description: Classes used in analyzing image pieces for reconstruction

import sys
import os
from PIL import Image
import operator
from collections import deque

from kernel import ImagePiece, RowBuilder, ImageRebuilder
		
			
# Main Kernel Functions
# ---------------------

def load_pieces(path):
	piece_names = os.listdir(path)
	img_pieces = deque()
	
	for piece in piece_names:
		img = Image.open(path + piece)
		img_piece = ImagePiece(img, piece[:-4])
		img_pieces.append(img_piece)
		img.close()
		
	return img_pieces

# Auxiliary Functions
# -------------------

def show_row(image_row, path):
	p_size = image_row[0].img.width
	n_pieces = len(image_row)
	img_width = p_size * n_pieces
	img = Image.new('RGB', (img_width, p_size))
	
	for i in range(len(image_row)):
		fpath = path + image_row[i].name + '.png'
		img_i = Image.open(fpath)
		img.paste(img_i, (i*p_size, 0))
			
	img.show()
	
	
def show_image(imagedata, path):
	pieces = imagedata.split(", ")
	canvas = Image.new('RGB', (512,512))
	for y in range(8):
		for x in range(8):
			imgname = pieces[y*8+x] + ".png"
			fpath = path + imgname
			img = Image.open(fpath)
			canvas.paste(img, (x*64, y*64))
			img.close()
	canvas.show()


def check_rows(rows, path):
	full_rows = list()
	for r in rows:
		if len(r.row) == 8:
			full_rows.append(r)
	
	if len(full_rows) == 8:
		return
	
	for r in full_rows:
		show_row(r.row, path)
	
	sys.exit(0)
	

# Main Driver
# -----------
def reconstruct_image():
	pathname = sys.argv[1]
	if len(pathname) == 0:
		print "No pathname given"
		sys.exit(0)
		
	path = os.getcwd() + '/tests/' + pathname + '/'
	pieces = load_pieces(path)
	
	rows = list()
	unfinished_rows = list()
	bailout = 0
	
	# Main logic to rebuild pieces into rows
	# version 0.3
	for i in range(8):
		row = RowBuilder(pieces)
		rowlen = len(row.row)
		
		if rowlen == 8:
			pieces = row.image_pieces
			row.name_row()
			rows.append(row)
		else:
			pieces = row.image_pieces
			row.clear_error()
			unfinished_rows.append(row)
		
		print "Row Attempt: %s - Pieces: %s" % (bailout, rowlen)
		if row.name != "":
			print row.name
		
	while bailout < 4:
		for row in unfinished_rows:
			row.pieces = pieces
			row.search_right()
			row.search_left()
			
			rowlen = len(row.row)
			if rowlen == 8:
				pieces = row.image_pieces
				row.name_row()
				rows.append(row)
				i_row = unfinished_rows.index(row)
				unfinished_rows.pop(i_row)
			else:
				row.clear_error()
		bailout += 1
		
	check_rows(rows, path)
	
	for row in rows:
		row.get_bounds()
	
	newImg = ImageRebuilder(rows)
	newImg.search_up()
	newImg.search_down()
	newImg.name_image()
	
	print "\n--------\n"
	print newImg.name
	
	show_image(newImg.name, path)

if __name__=='__main__':
	reconstruct_image()	

