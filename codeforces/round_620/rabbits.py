#!/usr/bin/python3

# Codeforces - Round 620
# Problem #1 - Two Rabbits


# Main
t = int(input())
for case in range(t):
	data = [int(x) for x in input().split(" ")]
	d = data[1] - data[0]
	a = data[2]
	b = data[3]
	
	if d % (a + b) != 0:
		print (-1)
	else:
		n = int(d / (a + b))
		print (n)
