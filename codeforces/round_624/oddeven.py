#!/usr/bin/python3

# Codeforces - Round 624
# Problem A - Add Odd or Subtract Even


# Main
t = int(input())
for case in range(t):
	data = [int(x) for x in input().split(" ")]
	a = data[0]
	b = data[1]
	
	if a == b:
		print (0)
	elif a > b and (a-b) % 2 != 0:
		print (2)
	elif b > a and (a-b) % 2 == 0:
		print (2)
	else:
		print (1)	
