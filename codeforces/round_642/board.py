#!/usr/bin/python3

# Codeforces - Round 642
# Problem C - Board Moves


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, arr):
	idx = (n)
		
	return sum(arr[:idx])


# Main
t = read_int()

#print (len(arr))

arr = [0] * (5 * pow(10, 5) + 1)
for i in range(3, 5 * pow(10, 5), 2):
	arr[i] = ((i-1) * 4) * (i // 2)

for case in range(t):
	n = read_int()
	sol = solve(n, arr)
	
	print (sol)
