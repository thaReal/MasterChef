#!/usr/bin/python3

# Codeforces - Codecraft 20
# Problem A - Grade Allocation


# Main
t = int(input())
for case in range(t):
	nm = [int(x) for x in input().split(" ")]
	n = nm[0]
	m = nm[1]
	
	a = [int(x) for x in input().split(" ")]
	score = min(sum(a), m)
	
	print (score)	
