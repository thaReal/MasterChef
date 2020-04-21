#!/usr/bin/python3
'''
Codejam 2020 - Round 1B
Problem: "Blindfolded Bullseye"
Author: Daniel Ruland
'''

# Only attempting cases 1 and 2

import sys
import os

# Global Variables

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
	

def check_adjacent(x, y, log):
	'''Check vertically adjacent and return case based on results
	Cases are: 0=tangent, 1-hit_up, 2-hit_down, 3-double_hit'''
	response1 = interact(x, y+1, log)
	response2 = interact(x, y-1, log)
	
	if response1 == "MISS" and response2 == "MISS":
		return 0
	elif response1 == "HIT" and response2 == "MISS":
		return 1
	elif response1 == "MISS" and response2 == "HIT":
		return 2
	else:
		return 3


def guess_center(x, y, log):
	'''given the x,y of the left tangent point, should interact and
	return a CENTER response from the judge'''
	x += A
	response = interact(x, y, log)
	if response == 'CENTER':
		return True
	
	
def seek_boundary(x, y, log):
	'''In the case that we reached x = +10 and we haven't had a hit yet,
	we step vertically until we find a point that intersects. As long as
	the step size is constant, it's impossible that we'll get a hit on both
	sides at the same step
	Output: coords of first HIT'''
	
	step = 1
	while step <= 10:
		response1 = interact(x, y+step, log)
		if response1 == 'HIT':
			return x, y+step

		response2 = interact(x, y-step, log)		
		if response2 == 'HIT':
			return x, y-step
		
		step += 1
		
	# basically at this ponit we're fucked, lets just bail
	sys.exit()
	
	

# Too fucking complicated, need a better approach	
def search(A, B, log):
	xmin = ymin = -1 * pow(10, 9)
	xmax = ymax = 1 * pow(10, 9)
	
	x = xmin
	y = 0
	response = interact(x, y, log)
	
	# find first itersection with horizontal axis
	while response == "MISS":
		x += 1
		response = interact(x, y, log)
		
		# If we don't hit by 10 steps, we need to see whether our dart
		# board is up or down
		if x == 10:
			x, y = seek_boundary(x, y, log)
			break
			
	# first 3 cases will all end with the correct solution being passed and 
	# the functioning returning. 4th case will move us back one and then move
	# up or down until we have an intersection. This should happen at most once
	# and 
	while True:
		result = check_adjacent(x, y, log)
		if result == 0:
			response = guess_center(x, y, log)
			if response:
				return
		
		elif result == 1:
			response = 'HIT'
			while response == 'HIT':
				y += 1
				response = interact(x, y, log)
		
			y -= 1
			y = round(y / 2)
			x -= 1
		
			response = interact(x, y, log)
			while response == 'HIT':
				x -= 1
				response = interact(x, y, log)
			x += 1
			response = guess_center(x, y, log)
			if response:
				return
		
		elif result == 2:
			response = 'HIT'
			while response == 'HIT':
				y -= 1
				response = interact(x, y, log)
			
			y += 1
			y = round(y / 2)
			x -= 1
		
			response = interact(x, y, log)
			while response == 'HIT':
				x -= 1
				response = interact(x, y, log)
			x += 1
			response = guess_center(x, y, log)
			if response:
				return


# Main
if os.path.exists('./logfile.txt'):
		os.remove('./logfile.txt')

log = open('logfile.txt', 'w') #debug
		
T, A, B = read_ints()
for i in range(T):
	log.write("Case: {}\n".format(i+1))
	search(A, B, log)
log.close()
