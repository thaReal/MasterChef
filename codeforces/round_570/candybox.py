#!/usr/bin/python
# Codeforces Round 570 (Div 3)
# Computer Game

from collections import defaultdict

def candysort(n, an):
	box = defaultdict(int)
	for ai in an:
		box[ai] += 1
	


#Main
q = int(raw_input())
for query in range(q)
	n = int(raw_input())
	an = [int(x) for x in raw_input().split(" ")]
	
	sol = candysort(n, an)
	print sol
