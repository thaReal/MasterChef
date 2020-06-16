#!/usr/bin/python3

# Codeforces - Round 650
# Author: frostD
# Problem D - Task on the Board 

from collections import Counter

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---



def solve(s, m, b):
	arr_t = ['0'] * m
	max_val = max(s)
	
	idx_0 = b.index(0)
	arr_t[idx_0] = max_val
	
	cntr = Counter(s)
	cntr[max_val] -= 1

	'''
	Needed to start with the highest letter at 0 and then iterate through array 
	b and pop min value, insert into arr_t and check, and repeat. May need to
	backtrack if subsequent values don't match the b value. I believe that 
	creating a counter from s to track the choice of values through each 
	iteration was a good choice of data structure, but that may change if I work
	through the actual implementation.
	'''
	
	
	t = ''.join(arr_t) #DEBUG
	
	return t


# Main
t = read_int()
for case in range(t):
	s = input()
	m = read_int()
	b = read_ints()
	sol = solve(s, m, b)
	print (sol)
