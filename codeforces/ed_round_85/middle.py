#!/usr/bin/python3

# Codeforces - Educational Round 85
# Problem B - Middle Class 


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints


def solve(n, x, a):
	wealthy = 0
	poor = []
	money = 0
	
	net = [i - x for i in a]
	for p in net:
		if p >= 0:
			wealthy += 1
			money += p
		else:
			poor.append(p)
	
	poor.sort()
	for i in poor:
		money += i
		if money >= 0:
			wealthy += 1
		else:
			break
			
	return wealthy
	
		

# Main
t = read_int()
for case in range(t):
	n, x = read_ints()
	a = read_ints()
	sol = solve(n, x, a)
	
	print (sol)
