#!/usr/bin/python3

# Codeforces - Round #675
# Author: frostD
# Problem B - Nice Matrix


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m, a):
	nice = [[0 for x in range(m)] for y in range(n)]
	
	for i in range(n // 2):
		for j in range(m // 2):
			nums = [a[i][j], a[i][m-j-1], a[n-i-1][j], a[n-i-1][m-j-1]]
			diffs = []
			for x in nums:
				diff = []
				for y in nums:
					diff.append(abs(x - y))
				diffs.append(sum(diff))

			min_diff = min(diffs)
			idx = diffs.index(min_diff)
			aij = nums[idx]
			
			nice[i][j] = aij
			nice[i][m-j-1] = aij
			nice[n-i-1][j] = aij
			nice[n-i-1][m-j-1] = aij
	
	
	if n % 2 == 1:
		r = n // 2 
		for i in range(m//2):
			aij = (a[r][i] + a[r][m-i-1]) // 2
			nice[r][i] = aij
			nice[r][m-i-1] = aij
	

	if m % 2 == 1:
		c = m // 2 
		for i in range(n//2):
			aij = (a[i][c] + a[n-i-1][c]) // 2
			nice[i][c] = aij
			nice[n-i-1][c] = aij
	
	if n % 2 == 1 and m % 2 == 1:
		nice[n//2][m//2] = a[n//2][m//2]
	
	#print (nice)
	
	diff = 0
	for i in range(n):
		for j in range(m):
			diff += abs(a[i][j] - nice[i][j])
	
	return diff
	



# Main
t = read_int()
for case in range(t):
	n, m = read_ints()
	a = []
	for i in range(n):
		ai = read_ints()
		a.append(ai)
		
	sol = solve(n, m, a)
	print (sol)
