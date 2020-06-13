#!/usr/bin/python3

# Codeforces - Round 649
# Author: frostD
# Problem C - Ehab and Prefix MEXs


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	b = []
	for i in range(n):
		rs = set(range(i+2))
		sb = rs.difference(set(b))
		if a[i] in sb:
			sb.remove(a[i])
		
		val = sb.pop()
		b.append(val)
		
		if a[i] in b:
			idx = b.index(a[i])
			for j in range(idx, i):
				b[j] += 1
		
	return b		


# Main
# !-

n = read_int()
a = read_ints()
sol = solve(n, a)

print (" ".join([str(x) for x in sol]))
