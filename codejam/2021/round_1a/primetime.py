#!/usr/bin/python3      

'''
Codejam 2021 - Round 1A
Problem: "Prime Time"
Author: Daniel Ruland
'''

# Utility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
# Solution:
from collections import deque

def solve(n, cards):
	score = 0
	q = deque()
	primes = list(cards.keys())
	
	for i in range(len(primes)):
		score1 = dict()
		score2 = dict()
		
				
	
	
	
	return score

# Main
T = read_int()
for i in range(T):
    m = read_int()
    cards = dict()
    for _ in range(m):
    	p, n = read_ints()
    	cards[p] = n
    
    sol = solve(n, cards)
	
	# Output
    print ("Case #{}: {}".format(i+1, sol))
