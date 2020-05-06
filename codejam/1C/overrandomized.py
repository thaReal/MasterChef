#!/usr/bin/python3
'''
Codejam 2020 - Round 1C
Problem: "Overrandomized"
Author: Daniel Ruland

*Post Competition Practice*
'''

from collections import Counter

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def solve(U, data):
	cntr = Counter()
	ltr_set = set()
	for elem in data:
		cntr[elem[1][0]] += 1
		if len(ltr_set) < 10:
			for i in elem[1]:
				ltr_set.add(i)
	
	ltr_map = dict()
	for ltr in ltr_set:
		if ltr not in cntr.keys():
			ltr_map[0] = ltr
			break

	
	for i in range(1, 10):
		mx = max(cntr.values())
		for k in cntr:
			if cntr[k] == mx:
				ltr_map[i] = k
				cntr[k] = 0
				break
	
	sol = ''
	for i in range(10):
		#print (ltr_map[i])
		sol += ltr_map[i]
		
	return sol



# Main
T = read_int()
for x in range(T):
	# Solution
	U = read_int()
	data = []
	for i in range(pow(10, 4)):
		val = input().split(" ")
		val[0] = int(val[0])
		data.append(val)
		
	sol = solve(U, data)
	
	# Output
	print ("Case #{}: {}".format(x+1, sol))
