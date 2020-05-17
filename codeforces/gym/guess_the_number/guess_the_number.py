#!/usr/bin/python3

# Codeforces: Gym 
# Problem 1 - Guess the Number [Interactive]

import sys

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def make_query(query):
	print (query)
	sys.stdout.flush()
	response = read_int()
	return response


def make_guess(guess):
	print ("! {}".format(guess))
	sys.stdout.flush()


#---

def solve(queries, mn, mx):
	q = 0
	# Need to implement binary search here

# Main
# ----

mn = 1
mx = 1000000
queries = 25
solve(queries, mn, mx)
