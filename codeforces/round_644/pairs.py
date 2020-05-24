#!/usr/bin/python3

# Codeforces - Round 644
# Problem C - Similiar Pairs 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	a.sort()
	
	evens = 0
	odds = 0
	one_off = 0
	
	for i in range(n):
		val = a[i]
		if val % 2:
			odds += 1
		else:
			evens += 1
		
		if i != 0:
			if a[i] - a[i-1] == 1:
				one_off += 1
		
	cnt = 0
	cnt += evens % 2
	cnt += odds % 2
	if cnt == 0:
		return "YES"
	
	while one_off > 0:
		odds -= 1
		evens -= 1
		
		cnt = 0
		cnt += evens % 2
		cnt += odds % 2
		if cnt == 0:
			return "YES"
		
		one_off -= 1
	
	return "NO"	
			


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	sol = solve(n, a)
	
	print (sol)
