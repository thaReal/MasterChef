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
	response = input()
	return response


def make_guess(guess):
	print ("! {}".format(guess))
	sys.stdout.flush()


#---

def solve(queries, mn, mx):
	q = 0
	li = mn
	ri = mx
	step = mx - mn
	guess = li
	while (ri - li) > 1:
		q += 1
		response = make_query(guess)
		if response == '>=':
			li = guess
		else:
			ri = guess
		
		step = (ri - li) // 2
		if q % 2:
			guess = ri - step
		else:
			guess = li + step
			
	if ri == mx:
		response = make_query(ri)
		if response == '>=':
			make_guess(ri)
		else:
			make_guess(li)
	else:
		make_guess(li)
	
	print ("Queries: {}".format(q))
	

		

# Main
# ----

mn = 1
mx = 1000000
queries = 25
solve(queries, mn, mx)
