#!/usr/bin/python

#Main

q = int(raw_input())
for i in range(q):
	n = int(raw_input())
	
	if n < 4:
		sol = 4 - n
		print sol
		continue
	
	if n % 2 == 0:
		print 0
	else:
		print 1
