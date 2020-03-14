#!/usr/bin/python3

# Codeforces - Round 628
# Problem A - EhAb AnD gCd


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints


# Main
t = read_int()
for i in range(t):
	x = read_int()
	a = str(x - 1)
	sol = "{} {}".format(a, 1)
	print (sol)
