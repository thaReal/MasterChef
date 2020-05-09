#!/usr/bin/python3

# Codeforces - Round 640
# Problem B - Same Parity Summands


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n,k):
	if k > n:
		return 'NO'
	
	n1 = 1
	nums = [n1] * (k-1)
	n2 = n - sum(nums)
	if n2 % 2 == 1 and n2 > 0:
		nums.append(n2)
		return [str(x) for x in nums]
	
	n1 = 2
	nums = [n1] * (k-1)
	n2 = n - sum(nums)
	if n2 % 2 == 0 and n2 > 0:
		nums.append(n2)
		return [str(x) for x in nums]
	
	return 'NO'
	


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	sol = solve(n, k)
	
	if sol == 'NO':
		print (sol)
	else:
		print ('YES')
		print (' '.join(sol))
