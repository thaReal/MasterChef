#!/usr/bin/python

def check_change(a, b, n, S):
	# check if our variable coins are worth at least S
	if a * n >= S:
		
		# if so, see if we have enough pennies to reach the total
		if b >= S % n:
			return "YES"
		
		else:
			return "NO"
			
	# otherwise check if we have enough combined coins 
	elif (a*n) + b >= S:
		return "YES"
	
	# otherwise it's not possible
	else:
		return "NO"

# Main
q = int(raw_input())
for i in range(q):
	line = [int(x) for x in raw_input().split(" ")]
	a = line[0]
	b = line[1]
	n = line[2]
	S = line[3]
	
	print check_change(a,b,n,S)
