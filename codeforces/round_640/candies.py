#!/usr/bin/python3

# Codeforces - Round 640
# Problem D - Alice, Bob, and Candies

from collections import deque


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, a):
	d = deque(a)
	alice = 0
	bob = 0
	
	alice_idx = 0
	bob_idx = n - 1
	
	turn = 0 #0: alice, 1: bob
	turns = 0
	last_candies = 0
	
	while len(d) > 0:
		pass
	'''
	while alice_idx <= bob_idx:
		#print ("bob: {}, alice: {}".format(bob_idx, alice_idx))
		turns += 1
		if turn == 0:
			cur_candies = a[alice_idx]
			alice_idx += 1
			while cur_candies < last_candies and alice_idx <= bob_idx:
				cur_candies = a[alice_idx]
				alice_idx += 1
				
			alice += cur_candies
			last_candies = cur_candies
			turn = 1 if turn == 0 else 0
			
		else:
			cur_candies = a[bob_idx]
			bob_idx -= 1
			while cur_candies < last_candies and alice_idx <= bob_idx:
				cur_candies = a[bob_idx]
				bob_idx -= 1
				
			bob += cur_candies
			last_candies = cur_candies
			turn = 1 if turn == 0 else 0
	'''		
	
	return [turns, alice, bob]


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	turns, alice, bob = solve(n, a)
	
	print ("{} {} {}".format(turns, alice, bob))
