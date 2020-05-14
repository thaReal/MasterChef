#!/usr/bin/python3

# Codeforces - Round 642
# Problem B - Two Arrays and Swaps


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, k, a, b):
	while k > 0:
		amin = min(a)
		bmax = max(b)
		if bmax <= amin:
			break
		
		i = a.index(amin)
		j = b.index(bmax)
		a[i], b[j] = b[j], a[i]
		k -= 1
	
	return sum(a)
	
		


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	a = read_ints()
	b = read_ints()
	sol = solve(n, k, a, b)
	
	print (sol)
