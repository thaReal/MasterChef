#!/usr/bin/python3

# Codeforces - Round 652
# Author: frostD
# Problem B - AccurateLee

from collections import deque

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, s):
	ls = [x for x in s[::-1]]
	while ''.join(ls).find('01') != -1:
		idx = ''.join(ls).find('01')
		if idx != 0:
			if ls[idx-1] == '0':
				ls.pop(idx-1)
				n -= 1
				continue
		
		if idx < n-2 and n > 2:	
			if ls[idx+2] == '1':
				ls.pop(idx+2)
				n -= 1
				continue
		
		ls.pop(idx+1)
		n -= 1
			
	return ''.join(ls[::-1])
	
	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	s = input()
	sol = solve(n, s)
	print (sol)
	
	
	
'''
	d = [x for x in s]
	i = 0
	while i < n:
		if d[i] == '0':
			i += 1
			continue
		
		if i < n-1:
			if d[i+1] == '0' and i != 0:
				if d[i-1] == '1':
					d.pop(i-1)
					i -= 1
					n -= 1
					continue
				
			if i < n-2:
				if d[i+2] == '0':
					d.pop(i+1)
					n -= 1
					continue
				
				else:
					d.pop(i)
					n -= 1
					continue
					
			elif d[i+1] == '0':
				d.pop(i)
				n -= 1
				continue
			
			else:
				i += 1
			
		else:
			i += 1
	
	return ''.join(d)
'''
