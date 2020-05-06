#!/usr/bin/python3

# Codeforces - Round 639
# Problem C - Hilbert's Hotel 

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	rms = []
	for k in range(n):
		rm =  a[k] + k % n
		rms.append(rm)
	
	if len(set(rms)) == len(rms):
		return 'YES'
	else:
		return 'NO'
	
# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n,a)
	
	print (sol)
