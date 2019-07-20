#!/usr/bin/python
from collections import deque

def solve(n, an):
	for i in range(n-2):
		if an[i] >= an[i+1] + an[i+2]:
			return "NO"
		return "YES"
		
def arrange(n, an):
	d = deque()
	for i in range(n):
		if i % 2 == 0:
			d.appendleft(an[i])
		else:
			d.append(an[i])
			
	return d

# Main
n = int(raw_input())	
an = [int(x) for x in raw_input().split(" ")]

an.sort(reverse=True)
sol = solve(n, an)
if sol == "YES":
	print sol
	ans = arrange(n, an)
	print " ".join([str(x) for x in ans])
else:
	print sol

