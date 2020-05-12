#!/usr/bin/python3

# Codeforces - Round 641
# Author - FrostD
# Problem B - Orac and Models 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(t, s):
	max_cnt = 1
	for i in range(t):
		curr_ind = i + 1
		curr_wt = s[ind-1]
		cnt = 1
		
		for j in range(2, t//2):
			ind = curr_ind * j
			while ind <= t:
				wt = s[ind-1]
				if wt > prev_wt:
					cnt += 1
					ind *= 2
					
	

# Main
t = read_int()
for case in range(t):
	t = read_int()
	s = read_ints()
	sol = solve(t, s)
	
	print (sol)
