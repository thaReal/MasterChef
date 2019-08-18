#!/usr/bin/python
from collections import deque

def generate_circle(n):
	odds = deque()
	for i in range(0, 2*n, 2):
		odds.append(i+1)
	
	evens = deque()
	for i in range(2*n, 0, -2):
		evens.append(i)
	
	sol = deque()
	for i in range(n):
		if i % 2 == 0:
			temp_l = odds.popleft()
			temp_r = evens.popleft()
			sol.appendleft(str(temp_l))
			sol.append(str(temp_r))
		else:
			temp_l = evens.popleft()
			temp_r = odds.popleft()
			sol.appendleft(str(temp_l))
			sol.append(str(temp_r))
	
	# convert deque to output string
	outstr = " ".join(sol)
	return outstr	


# Main
n = int(raw_input())
if n % 2 == 0:
	print "NO"
else:
	circle = generate_circle(n)
	print "YES"
	print circle
