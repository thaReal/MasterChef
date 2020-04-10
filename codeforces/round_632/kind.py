#!/usr/bin/python3

# Codeforces - Round 632
# Problem B - Kind Anton 


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

def solve(n, a, b):
	if a[0] != b[0]:
		return 'NO'
				
	try:
		pos = a[1:].index(1)
	except:
		pos = None
	
	try:
		neg = a[1:].index(-1)
	except:
		neg = None
	
	# 4 Cases
	if pos != None:
		if max(b[:pos+1]) > 0:
			print ("CASE 1")
			return 'NO'
	else:
		if max(b) > 0:
			print ("CASE 2")
			return 'NO'
	 	
	if neg != None:
		if min(b[:neg+1]) < 0:
			print ("CASE 3")
			return 'NO'

	else:
		if min(b) < 0:
			print ("CASE 4")
			return 'NO'
	
	return 'YES'

'''
def solve(n, a, b):
	if a[0] != b[0]:
		return 'NO'
		
	for i in range(1, n):
		if 1 in set(a[:i]) and -1 in set(a[:i]):
			return 'YES'
		
		if a[i] != b[i]:
			if a[i] > b[i]:
				if -1 not in set(a[:i]):
					return 'NO'		
			else:
				if 1 not in set(a[:i]):
					return 'NO'
	
	return 'YES'
'''
	
# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	b = read_ints()
	
	sol = solve(n, a, b)
	print (sol)
