#!/usr/bin/python3
'''
Codejam 2020 - Round 1C
Problem: "" [Interactive]
Author: Daniel Ruland
'''

import sys
import os

# Input Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints


# Interact function (w/ logging)
def interact(x, y, log):
	log.write("{} {}\n".format(x, y)) #Debug
	print ("{} {}".format(x, y))
	sys.stdout.flush()

	response = input()
	log.write("{}\n".format(response)) #Debug
	
	if response == 'WRONG':
		log.close()
		sys.exit()

	return response


# Main Solver Function
def solve(A, log):
	pass




#------
# Main
#------

if os.path.exists('./logfile.txt'):
		os.remove('./logfile.txt')

log = open('logfile.txt', 'w') #debug
		
T = read_int()
for i in range(T):
	log.write("Case: {}\n".format(i+1))
	
	data = read_ints()
	log.write("{}".format(data))
	
	solve(A, B, log)
	
log.close() #Debug
