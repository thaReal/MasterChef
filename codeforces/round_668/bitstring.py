#!/usr/bin/python3

# Codeforces - Round# 668
# Author: frostD
# Problem C - Balanced Bitstring 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, k, s):
	a = []
	for char in s:
		try:
			a.append(int(char))
		
		except:
			a.append('')
			
			
	for i in range(0, n-k+1):
		substr = a[i:i+k]
		sm = 0
		wild = 0
		
		for j in substr:
			try:
				sm += j
			except:
				wild += 1
		
		# Debug
		#print ("substr: {}".format(substr))
		#print ("sm: {}, wild: {}".format(sm, wild))
		
		if sm + wild >= k // 2 and sm - wild <= k // 2:
			continue
		
		return 'NO'
		
	return 'YES'
	


# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	s = input() #string
	
	sol = solve(n, k, s)
	print (sol)
