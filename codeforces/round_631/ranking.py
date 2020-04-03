#!/usr/bin/python3

# Codeforces - Round 631
# Problem A - Dreamoon and Ranking Collection

# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def solve():
	pass
	

# Main
t = read_int()
for case in range(t):
	n, x = read_ints()
	a = read_ints()
	
	pos = set(a)
	v = 1
	while x > 0:
		if v in pos:
			v += 1
		else:
			x -= 1
			if x > 0:
				v += 1
	
	while True:
		if v+1 in pos:
			v += 1 
		else:
			break
		
	print (v)	
