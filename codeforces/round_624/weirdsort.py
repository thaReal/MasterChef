#!/usr/bin/python3

# Codeforces - Round 624
# Problem B - WeirdSort 


def weirdsort(a,b):
	for i in range(len(a)-1):
		if i+1 in b:
			continue

		s1 = a[0:i+1]
		s2 = a[i+1::]
		if max(s1) > min(s2):
			return "NO"
		
	return "YES"
	

# Main
t = int(input())
for case in range(t):
	nm = [int(x) for x in input().split(" ")]
	n = nm[0]
	m = nm[1]
	 
	a = [int(x) for x in input().split(" ")]
	p = [int(x) for x in input().split(" ")]
	
	print (weirdsort(a,p))
