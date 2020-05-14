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
	idx = (n - 1) // 2
		
	return sum(arr[:idx])


# Main
t = read_int()

arr = [0] * 25 * pow(10, 4)
print (len(arr))
for i in range(3, 25 * pow(10, 4) - 1, 2):
	arr[i] = 2**i

for case in range(t):
	n = read_int()
	sol = solve(n, arr)
	
	print (sol)
