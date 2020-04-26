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
	

def check_adjacent(x, y, log, step=1):
	'''Check vertically adjacent coordinates'''
	response1 = interact(x, y+step, log)
	response2 = interact(x, y-step, log)
	
	r1 = 1 if repsonse1 == 'HIT' else 0
	r2 = 1 if repsonse2 == 'HIT' else 0
	
	return r1, r2


def guess_center(x, y, log):
	'''given the x,y of the left tangent point, should interact and
	return a CENTER response from the judge'''
	x += A
	response = interact(x, y, log)
	if response == 'CENTER':
		return True
	

def search(A, B, log):
	xmin = ymin = -1 * pow(10, 9)
	xmax = ymax = 1 * pow(10, 9)
	
	x = xmin
	y = 0
	direction = None #1 for up, -1 for down, None initially
	
	response = interact(x, y, log)
	
	# find first itersection with horizontal axis
	while response == "MISS":
		x += 1
		response = interact(x, y, log)
		
		if response == 'HIT':
			r1, r2 = check_adjacent(x, y, log, step=step)
			if r1 == 0 and r2 == 0:
				response = guess_center(x, y, log)
				if response:
					return
				else:
					sys.exit()
		
		# If we don't hit by 10 steps, we've reached max x
		if x == 10:
			break
		
	# reached our first intersection point with circle
	step = 1
	while direction == None:
		r1, r2 = check_adjacent(x, y, log, step=step)
		if r1 == 1 and r2 == 1:
			x -= 1
			step = 1
			
		elif r1 == 1:
			direction = 1
			y = y + step
			
		elif r2 == 1:
			direction = -1
			y = y - step
			
		else:
			step += 1
	
	# Now we're at least as far +x as we need to be and moving in the 
	# correct y direction -> need to move +/-y and -x until we find tangent
	
	y += direction
	response = interact(x, y, log)
	while True:
		if response == "HIT":
			x -= 1
			continue
		
		if response == "MISS":
			
	
	
	
	
	
	

# Main
if os.path.exists('./logfile.txt'):
		os.remove('./logfile.txt')

log = open('logfile.txt', 'w') #debug
		
T, A, B = read_ints()
for i in range(T):
	log.write("Case: {}\n".format(i+1))
	search(A, B, log)
log.close()
