#!/usr/bin/python3

# Codeforces - Round 632
# Problem C - Eugene and an Array


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def solve(n, a):
	cnt = 0
	il = 0
	ir = il + 1
	while il < n:
		while ir <= n:
			if sum(a[il:ir]) != 0:
				cnt += ir - il
				ir += 1
			else:
				break
			
		il += 1
		if il == ir:
			ir += 1
			
	return cnt
			
	

# Main
n = read_int()
a = read_ints()
print (solve(n,a))
