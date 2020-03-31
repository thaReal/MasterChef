#!/usr/bin/python3

# Codeforces - Round 630
# Problem B - Composite Coloring

from math import gcd

# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

def solve(n, a):
	color = 1
	colors = [color for x in a]
	
	while colors.count(color) > 0:
		coprimes = []
		for i in range(len(a) - 1):
			a0 = a[i]
			a1 = a[i+1]
			c = gcd(a0, a1)
			coprimes.append(c)
	
		for i in range(len(coprimes)):
			if coprimes[i] == 1:
				colors[i+1] = color
		
		color += 1 
	
	print (colors)
	
	
def test(n, a):
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
	
	for p in primes:
		pass	
		


# Main
t = read_int()
for i in range(t):
	n = read_int()
	a = read_ints()
	test(n, a)
