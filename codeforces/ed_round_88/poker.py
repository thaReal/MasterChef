#!/usr/bin/python3

# Codeforces - Educational Round 88
# Author: frostD
# Problem A - Berland Poker

from math import ceil

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, m, k):
	if m == 0:
		return 0
	hand_sz = n // k
	
	if hand_sz >= m:
		jokers = m
	else:
		jokers = hand_sz
	
	rem_jokers = m - jokers
	if rem_jokers == 0:
		score = jokers
	
	else:
		score = jokers - ceil((rem_jokers / (k-1)))
	
	return score


# Main
t = read_int()
for case in range(t):
	n, m, k = read_ints()
	sol = solve(n, m, k)
	print (sol)
