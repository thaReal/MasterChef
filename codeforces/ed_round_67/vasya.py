#!/usr/bin/python
from collections import Counter

compare = lambda x, y: Counter(x) == Counter(y)

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
			asub = [an[i]]
			bsub = [bn[i]]
			smax = an[i]
			i += 1
			
		else:
			asub.append(an[i])
			bsub.append(bn[i])
			if compare(asub, bsub) == False:
				if an[i] >= smax or bn[i] >= smax:
					break			
				i += 1
			else:
				sol = "YES"
				subsort = False
				i += 1
				
	print sol
