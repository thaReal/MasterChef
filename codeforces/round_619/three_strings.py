#!/usr/bin/python3

# Codeforces Round 619
# Problem #1 - Three Strings

t = int(input())
for case in range(t):
	a = input()
	b = input()
	c = input()
	
	sol = "YES"
	for i in range(len(a)):
		if c[i] != a[i] and c[i] != b[i]:
			sol = "NO"
			break
	print (sol)
