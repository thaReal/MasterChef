#!/usr/bin/python3
'''
Codejam 2020 Qualification Round 
Problem: "ESAb ATAd"
Author: Daniel Ruland
'''
import sys
from collections import deque

def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def query(pos):
	print (pos)
	sys.stdout.flush()
	response = int(input())
	
	return response
	
	
def reverse_opr(a):
	l = len(a)
	for i in range(l // 2):
		i0 = a[i]
		i1 = a[l-1-i]
		a[i] = i1
		a[l-1-i] = i0
	
	return a
		
	
def compliment_opr(a):
	for i in range(len(a)):
		a[i] = 1 if a[i] == 0 else 0
	
	return a
	
	
def discover_fluctuation(sol, B):
	c_pair = None
	r_pair = None
	offset = (B - len(sol)) // 2
	
	# search for equal and unequal number pairs
	i = 0
	while i < len(sol) // 2:
		l1 = sol[i]
		l2 = sol[-i-1]
		
		if c_pair == None:
			if l1 == l2:
				c_pair = i
		
		if r_pair == None:
			if l1 != l2:
				r_pair = i
		
		if c_pair != None and r_pair != None:
			break
	
		i += 1
	
	# Determine the type of fluctuation that has occured
	
	# compliment and reverse give the same result; both do nothing
	if c_pair == None:
		# check r_pair
		val1 = query(r_pair + offset + 1)
		val2 = query(B - offset - r_pair + 1)
		
		if val1 == sol[r_pair]:
			reverse = True
		else:
			reverse = False
		compliment = False
		
	# reverse does nothing; doint both is the same as doing compliment
	elif r_pair == None:
		val1 = query(c_pair + offset + 1)
		val2 = query(B - offset - c_pair + 1)
		
		if val1 == sol[c_pair]:
			compliment = True
		else:
			compliment = False
		reverse = False
		
	# both have an effect; need to check respective pairs to determine opr
	else:
		# lets check c_pair first
		val1 = query(c_pair + offset + 1)
		val2 = query(r_pair + offset + 1)
		
		if val1 == sol[c_pair]:
			if val2 == sol[r_pair]:
				compliment = False
				reverse = False
			else:
				compliment = False
				reverse = True
		else:
			if val2 == sol[r_pair]:
				compliment = True
				reverse = True
			else:
				compliment = True
				reverse = False
		
		
	# Perform fluctuation operations on our current solution	
	if reverse:
		sol = reverse_opr(sol)
			
	if compliment:
		sol = compliment_opr(sol)
			
	return sol



def solve(B):
	sol = deque()
	idx = B // 2
	unknown = False
	q = 1
	
	sol.append(query(idx))
	while len(sol) < B or unknown == True:
		# unknown is flipped True when we experience a fluctuation
		# Then we need to query positions to determine fluctuation type
		# and apply to our existing solution to flip back
		if unknown:
			sol = discover_fluctuation(sol, B)
			q += 2
			
			if len(sol) == B:
				break
		
		# index positions step out from the middle
		idx *= -1
		if idx < 0:
			idx += 1
			val = query(B+idx)
			sol.append(val)
		else:
			val = query(idx)
			sol.appendleft(val)
		
		q += 1
		
		if q % 10 == 1:
			unknown = True
	
	
	# Once loop is complete we should have our full, validated array
	print (''.join([str(x) for x in sol]))
	sys.stdout.flush()
	response = input()
	
	# In case of error, exit before returning
	if response == 'N':
		sys.exit()
	else:
		return
	


# Main
T, B = read_ints()
for x in range(T):
	solve(B)
	
	
