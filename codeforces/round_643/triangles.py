#!/usr/bin/python3

# Codeforces - Round #643
# Problem C - Count Triangles 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(a, b, c, d):
	k_max = b + c
	i_min = k_max - b

	cnt = (b - max(i_min, a) + 1) * (c - b + 1) * (min(k_max, d) - c + 1)
				
	return cnt
	

# Main
a, b, c, d = read_ints()
sol = solve(a, b, c, d)

print (sol)
