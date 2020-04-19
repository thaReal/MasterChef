#!/usr/bin/python3
'''
Codejam 2020 - Round 1B
Problem: "Blindfolded Bullseye"
Author: Daniel Ruland
'''

# Only attempting cases 1 and 2

import sys
import os
from math import pi, sqrt

# Global Variables
xmin = ymin = -2 * pow(10, 9)
xmax = ymax = 2 * pow(10, 9)

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def interact(x, y, log):
	log.write("{} {}\n".format(x, y)) #debug
	
	print ("{} {}".format(x, y))
	sys.stdout.flush()

	response = input()
	log.write("{}\n".format(response))
	
	if response == 'WRONG':
		log.close()
		sys.exit()

	return response
	
	
def search():
	if os.path.exists('./logfile.txt'):
		os.remove('./logfile.txt')
		
	log = open('logfile.txt', 'w') #debug
	x = 0
	y = 0
	response = interact(x, y, log)
	
	mesh_sz = 4
	while response == "MISS":
		mesh = [0] * mesh_sz
		mesh_pts = []
		step = (xmin - ymin) // sqrt(mesh_sz)
		for i in range(step):
			x = i * step
			for j in range(step):
				y = j * step
				mesh_pts.append((x,y))
		
		for pt in mesh_pts:
			response = interact(pt[0], pt[1], log)
			if response != 'MISS':
				x, y = pt
				break
				
		mesh_sz *= 2	
	
	log.close() #debug
	return x, y, response

def process_case(A, B):
	dia = 2 * pi * A
	x, y, response = search()
	if response != 'CENTER':
		sys.exit()

# Main
T, A, B = read_ints()
for i in range(T):
	process_case(A, B)
