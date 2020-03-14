#!/usr/bin/python3

# Codeforces - Round 628
# Problem B - CopyCopyCopyCopyCopy 


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
	n = read_int()
	a = read_ints()
	print (len(set(a)))
