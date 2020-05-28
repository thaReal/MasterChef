#!/usr/bin/python3

# Codeforces - Educational Round 88
# Author: frostD
# Problem B - New Theatre Square


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m, x, y, a):
	A = []
	for row in a:
		nrow = []
		for char in row:
			if char == '*':
				nrow.append(0)
			else:
				nrow.append(1)
		A.append(nrow)
		
	if y >= 2 * x:
		res = 0
		for row in A:
			res += sum(row)	
		return res * x
	
	else:
		res = {1: 0, 2: 0} 
		for row in A:
			i = 0
			while i < m:
				if i != m - 1:
					if row[i] + row[i+1] == 2:
						res[2] += 1
						i += 2
					elif row[i] == 1:
						res[1] += 1
						i += 2
					else:
						i += 1
				
				else:
					if row[i] == 1:
						res[1] += 1	
					i += 1
					
		return res[1] * x + res[2] * y
			


# Main
t = read_int()
for case in range(t):
	n, m, x, y = read_ints()
	a = []
	for i in range(n):
		row = input()
		a.append(row)
		
	sol = solve(n, m, x, y, a)
	print (sol)
