#!/usr/bin/python
from collections import Counter

t = int(raw_input())
for q in range(t):
	n = int(raw_input())
	an = [int(x) for x in raw_input().split(" ")]
	bn = [int(x) for x in raw_input().split(" ")]
	
	sol = "YES"
	i = 0
	smax = 0
	subsort = False
	
	while i < n:
		if subsort == False:
			if an[i] == bn[i]:
				i += 1
				continue
			
			if bn[i] > an[i]:
				sol = "NO"
				break
			
			subsort = True
			sol = "NO"
			
			asub = Counter()
			asub[an[i]] += 1
			bsub = Counter()
			bsub[bn[i]] += 1
			smax = an[i]
			
			i += 1
			
		else:
			asub[an[i]] += 1
			bsub[bn[i]] += 1
			if asub != bsub:
				i += 1
				
			else:
				sol = "YES"
				subsort = False
				i += 1
				
	print sol
