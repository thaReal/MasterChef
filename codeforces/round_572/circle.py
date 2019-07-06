#!/usr/bin/python

from collections import deque

def solve(n, an):
	sol = None
	bn = deque()
	an.sort()
	
	for i in range(n):
		if i <= 3:
			bn.append(an[i])
			continue
			
		if bn[i-1] + bn[i-2] < an:
			bn.append(an[i])
		else:
			bn.appendleft(an[i])
	
	for i in range(n):
		bi = bn[i]
		bleft = bn[i-1]
		if i+1 != n:
			bright = bn[i+1]
		else:
			bright = bn[0]
		if bi >= bleft + bright:
			return ("NO", None)
	
	output = [str(x) for x in bn]	
	return ("YES", output)
		

#Main
n = int(raw_input())
an = [int(x) for x in raw_input().split(" ")]
sol = solve(n, an)

if sol[0] == "NO":
	print "NO"
else:
	print sol[0]
	print " ".join(sol[1])
