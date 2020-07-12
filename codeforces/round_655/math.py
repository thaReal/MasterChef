#!/usr/bin/python3

# Codeforces - Round 655
# Author: frostD
# Problem B - Omkar and Last Class of Math

from math import sqrt

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---
def get_divisors(n):
	i = 1
	divisors = set()
	while i*i <= n:
		if n % i == 0:
			divisors.add(i)
			divisors.add(n // i)
		i += 1
	
	divisor_list = list(divisors)
	divisor_list.sort()
	divisor_list.pop()
	
	return divisor_list[::-1]
	

def solve(n):
	# if n is even
	if n % 2 == 0:
		return [str(n // 2), str(n // 2)]
	
	divisors = get_divisors(n)

	for a in divisors:
		b = n - a
		if b % a == 0:
			return [str(a), str(b)] 
	
	
	'''
	# else if its a perfect square
	if sqrt(n) == int(sqrt(n)):
		return [str(int(sqrt(n))), str(int(n - sqrt(n)))] 
		
	a = (n // 2)
	if a % 2 == 0:
		a -= 1
	b = n - a
	while b % a != 0:
		a -= 2
		b = n - a
	'''
	
	return [str(a), str(b)]
		
		


# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n)
	print (' '.join(sol))
