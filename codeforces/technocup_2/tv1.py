#!/usr/bin/python


# Main
t = int(raw_input())
for i in range(t):
	l1 = [int(x) for x in raw_input().split(" ")]
	n = l1[0]
	k = l1[1]
	d = l1[2]
	
	a = [int(x) for x in raw_input().split(" ")]
	ms = d # minimum subscriptions; worst case is 1 per day
	
	for j in range(n-d+1):
		ai = a[j:j+d]
		ms = min(ms, len(set(ai)))
		
	print ms
