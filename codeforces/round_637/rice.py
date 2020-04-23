#!/usr/bin/python3

# Codeforces - Round 637
# Problem A - Nastya and Rice


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n,a,b,c,d):
	gmin = a - b
	gmax = a + b
	
	wmin = c - d
	wmax = c + d
	
	if gmax * n < wmin or gmin * n > wmax:
		return False
	else:
		return True
	


# Main
t = read_int()
for case in range(t):
	n, a, b, c, d = read_ints()
	sol = solve(n,a,b,c,d)
	
	if sol:
		print ('Yes')
	else:
		print ('No')
