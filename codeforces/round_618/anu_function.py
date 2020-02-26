#!/usr/bin/python3

# Codeforces - Round 618
# Problem A - Anu has a Function


def f(x, y):
	ans = (x | y) - y
	return ans
	

# Main
n = int(input())
a = [int(x) for x in input().split(" ")]

output = []
while len(a) > 1:
	x = max(a)
	x_i = a.index(x)
	a.pop(x_i)
	
	mx = 0
	for y in a:
		mx = max(mx, f(x,y))
	
	y_i = a.index(y)
	a.pop(y_i)
	a.append(mx)

print (a[0])
	
