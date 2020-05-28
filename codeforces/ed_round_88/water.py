#!/usr/bin/python3

# Codeforces - Educational Round 88
# Author: frostD
# Problem C - Mixing Water

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(h, c, t):
	if h == t:
		return 1

	tconv = (h+c) / 2
	if t <= tconv:
		return 2		
	
	barrel = []
	deltas = []
	while True:
		barrel.append(h)
		tb = sum(barrel) / len(barrel)
		tdelta = abs(t - tb)
		if tdelta == 0:
			return len(barrel)
		
		print(tdelta) #debug
		deltas.append(tdelta)
		
		if len(deltas) > 1:
			if deltas[-1] >= deltas[-2]:
				break
		
		barrel.append(c)
		tb = sum(barrel) / len(barrel)
		tdelta = abs(t - tb)
		if tdelta == 0:
			return len(barrel)
		
	return (len(deltas) - 2) * 2 + 1
	
	
	
# Main
t = read_int()
for case in range(t):
	h, c, t = read_ints()
	sol = solve(h, c, t)
	
	print (sol)
