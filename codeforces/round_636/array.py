#!/usr/bin/python3

# Codeforces - Round 636
# Problem B - Balanaced Array 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n):
	sz = n // 2
	if sz % 2 == 1:
		return "NO"
	
	arr1 = [x for x in range(2, 2*sz+1, 2)]
	arr2 = [x for x in range(1, 2*sz, 2)]
	
	if sum(arr1) > sum(arr2):
		diff = sum(arr1) - sum(arr2)
		arr2[-1] += diff
	
	arr = arr1 + arr2
	sol = " ".join([str(x) for x in arr])
	
	return ('YES', sol)
	
		
	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	sol = solve(n) #tuple (str, arr) if found, else str
	
	if sol == 'NO':
		print (sol)
	else:
		print(sol[0])
		print(sol[1])
