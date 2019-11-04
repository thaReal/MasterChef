#!/usr/bin/python

# kernel.py: Danny Ruland
# Description: Core classes for processing image pieces for reconstruction

import sys
import os
from PIL import Image
import operator
from collections import deque


class ImagePiece(object):
	def __init__(self, img, name):
		self.img = img
		self.name = name
		self.size = img.width
		
		self.ubound = list()
		self.dbound = list()
		self.lbound = list()
		self.rbound = list()
		self.get_bounds()
		
		self.lerror = dict()
		self.rerror = dict()
		self.img.close()
		
	def get_bounds(self):
		for i in range(self.size):
			l_pixel = self.img.getpixel((0, i))
			r_pixel = self.img.getpixel((self.size-1, i))
			u_pixel = self.img.getpixel((i, 0))
			d_pixel = self.img.getpixel((i, self.size-1))
			
			self.lbound.append(l_pixel)
			self.rbound.append(r_pixel)
			self.ubound.append(u_pixel)
			self.dbound.append(d_pixel)
		
	# debug functions		
	def print_lbound(self):
		cnt = 0
		for i in self.lbound:
			print "0, %s: %s" % (cnt, i)
			cnt += 1
			
	def print_rbound(self):
		cnt = 0
		for i in self.rbound:
			print "63, %s: %s" % (cnt, i)
			cnt += 1


class RowBuilder(object):
	def __init__(self, image_pieces):
		self.row = deque()
		p0 = image_pieces.pop()
		self.row.append(p0)
		self.image_pieces = list(image_pieces)
		self.name = ""
		
		self.ubound = list()
		self.dbound = list()
		self.uerror = dict()
		self.derror = dict()
		
		# initialize left and right error lists
		for i in range(len(self.image_pieces)):
			compare_bounds(self.row[0], self.image_pieces[i])
			compare_bounds(self.image_pieces[i], self.row[0])
		
		self.lerror = self.row[0].lerror
		self.rerror = self.row[0].rerror
		
		# attempt to build the row until the min error back-check method
		# fails or we succesfully found 8 pieces
		self.search_right()
		self.search_left()
		
	def clear_error(self):
			self.image_pieces[0].lerror = dict()
			self.image_pieces[-1].rerror = dict()
	
		
	def search_right(self):
		while len(self.row) < 8:
			# find the best candidate (that hasn't already been used in
			# a reconstructed row
			candidate = None
			while candidate == None:
				min_error = min(self.rerror.values())
				for k,v in self.rerror.items():
					if v == min_error:
						candidate_name = k
						break
			
				for piece in self.image_pieces:
					if piece.name == candidate_name:
						candidate = piece
						break
			
				if candidate == None:
					self.rerror.pop(candidate_name)
			
			# perform a reverse search on our candidate pieces
			for piece in self.image_pieces:
				if piece.name != candidate_name:
					compare_bounds(candidate, piece)
					compare_bounds(piece, candidate)
			
			# Then check that the min error matches. If it does,
			# add to row and continue
			if min(candidate.lerror.values()) == min_error:	
				self.row.append(candidate)
				i_candidate = self.image_pieces.index(candidate)
				self.image_pieces.pop(i_candidate)
				self.rerror = candidate.rerror
				
			else:
				break
				
	def search_left(self):
		while len(self.row) < 8:
			# find the best candidate (that hasn't already been used in
			# a reconstructed row
			candidate = None
			while candidate == None:
				min_error = min(self.lerror.values())
				for k,v in self.lerror.items():
					if v == min_error:
						candidate_name = k
						break
			
				for piece in self.image_pieces:
					if piece.name == candidate_name:
						candidate = piece
						break
				
				if candidate == None:
					self.rerror.pop(candidate_name)
			
			# Now perform a reverse search on our candidate pieces
			for piece in self.image_pieces:
				if piece.name != candidate.name:
					compare_bounds(candidate, piece)
					compare_bounds(piece, candidate)
			
			if min(candidate.rerror.values()) == min_error:
				# Then double check matches, add to row and continue
				self.row.appendleft(candidate)
				i_candidate = self.image_pieces.index(candidate)
				self.image_pieces.pop(i_candidate)
				self.lerror = candidate.lerror
				
			else:
				break
				
	def get_bounds(self):
		for piece in self.row:
			self.ubound += piece.ubound
			self.dbound += piece.dbound
			
	def name_row(self):
		name_lst = list()
		for piece in self.row:
			name_lst.append(piece.name)
		self.name = ", ".join(name_lst)
			
			
class ImageRebuilder(object):
	def __init__(self, rows):
		self.image = deque()
		r0 = rows.pop()
		self.image.append(r0)
		self.rows = rows
		
		# initialize up and down error lists
		for i in range(len(self.rows)):
			compare_row_bounds(self.image[0], self.rows[i])
			compare_row_bounds(self.rows[i], self.image[0])
		
		self.uerror = self.image[0].uerror
		self.derror = self.image[0].derror
	
		
	def search_up(self):
		while len(self.image) < 8:
			min_error = min(self.uerror.values())
			for k,v in self.uerror.items():
				if v == min_error:
					candidate_name = k
					break
			
			for row in self.rows:
				if row.name == candidate_name:
					candidate = row
					break
					
			for row in self.rows:
				if row.name != candidate.name:
					compare_row_bounds(candidate, row)
					compare_row_bounds(row, candidate)
			
			if min(candidate.derror.values()) == min_error:
				# Then double check matches, add to image and continue
				self.image.appendleft(candidate)
				i_candidate = self.rows.index(candidate)
				self.rows.pop(i_candidate)
				self.uerror = candidate.uerror
				
			else:
				break
	
	
	def search_down(self):
		while len(self.image) < 8:
			min_error = min(self.derror.values())
			for k,v in self.derror.items():
				if v == min_error:
					candidate_name = k
					break
			
			for row in self.rows:
				if row.name == candidate_name:
					candidate = row
					break
					
			for row in self.rows:
				if row.name != candidate.name:
					compare_row_bounds(candidate, row)
					compare_row_bounds(row, candidate)
			
			if min(candidate.uerror.values()) == min_error:
				# Then double check matches, add to image and continue
				self.image.append(candidate)
				i_candidate = self.rows.index(candidate)
				self.rows.pop(i_candidate)
				self.derror = candidate.derror
				
			else:
				break
	
	def name_image(self):
		name_lst = list()
		for row in self.image:
			name_lst.append(row.name)
		self.name = ", ".join(name_lst)
		
		
def compare_bounds(img0, img1):
	'''
	Compare the error of the right bound of img0 to the left bound of img1
	and sets the respective values in their error dictionaries
	'''
	rbound = img0.rbound
	lbound = img1.lbound
	
	error = 0
	for i in range(len(rbound)):
		# need to wrap operator.sub in abs(), want to make sure
		# that everything works first though
		error_v = map(operator.sub, rbound[i], lbound[i])
		abs_error = [abs(x) for x in error_v]
		error += sum(abs_error)
	
	img0.rerror[img1.name] = error
	img1.lerror[img0.name] = error
	
	
def compare_row_bounds(row0, row1):
	'''
	Compare the error of the upper bound of row0 to the lower bound of row1
	and sets the respective values in their error dictionaries
	'''
	ubound = row0.ubound
	dbound = row1.dbound
	
	error = 0
	for i in range(len(ubound)):
		error_v = map(operator.sub, ubound[i], dbound[i])
		abs_error = [abs(x) for x in error_v]
		error += sum(abs_error)
		
	row0.uerror[row1.name] = error
	row1.derror[row0.name] = error
