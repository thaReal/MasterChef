#!/usr/bin/python3
'''
Codejam 2020 - Round 1B
Problem: "Blindfolded Bullseye"
Author: Daniel Ruland
'''

# Only attempting cases 1 and 2

import sys
import os
from math import sqrt


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
	

def check_adjacent(x, y, log, step=1):
	'''Check vertically adjacent coordinates'''
	response1 = interact(x, y+step, log)
	response2 = interact(x, y-step, log)
	
	r1 = 1 if response1 == 'HIT' else 0
	r2 = 1 if response2 == 'HIT' else 0
	
	return r1, r2


def guess_center(x, y, log):
	'''given the x,y of the left tangent point, should interact and
	return a CENTER response from the judge'''
	x += A
	
	log.write('Guess: x={}, y={}\n'.format(x+A//2, y))
	
	response = interact(x, y, log)
	if response == 'CENTER':
		return True
		
		
def find_cp(x1, y1, x2, y2, r):
	q = sqrt(pow(x2-x1, 2) - pow(y2-y1, 2)
	x3 = (x1 + x2) / 2
	y3 = (y1 + y2) / 2
	
	
	x = x3 - sqrt(pow(r, 2) - pow((q/2), 2) * (y1-y2) / q)
	y = y3 - sqrt(pow(r, 2) - pow((q/2), 2) * (x2-x1) / q)  
	
	return (x, y)
	
	

def solve(A, B, log):
	xmin = ymin = -1 * pow(10, 9)
	xmax = ymax = 1 * pow(10, 9)
	max_offset = (xmax - xmin) - (A * 2)
	
	x = xmin
	y = 0
	direction = None #1 for up, -1 for down, None initially
	
	response = interact(x, y, log)
	
	# ---
	
	
	
	
	

# Main
if os.path.exists('./logfile.txt'):
		os.remove('./logfile.txt')

log = open('logfile.txt', 'w') #debug
		
T, A, B = read_ints()
for i in range(T):
	log.write("Case: {}\n".format(i+1))
	log.write("A: {}, B: {}\n".format(A, B))
	solve(A, B, log)
log.close()
