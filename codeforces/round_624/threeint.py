#!/usr/bin/python3

# Codeforces - Round 624
# Problem D - Three Integers

from math import ceil, floor

# Main
t = int(input())
for case in range(t):
	abc = [int(x) for x in input().split(" ")]
	a = abc[0]
	b = abc[1]
	c = abc[2]
	
	case1 = []
	case2 = []
	if c % b == 0:
		case1.append(c)
		case2.append(c)
	else:
		case1.append(floor(c/b))
		case2.append(ceil(c/b))
		
# Times up, this is a start but probably need to work outwards from the 
# middle number (b)
