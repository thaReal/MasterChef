#!/usr/bin/python3

# Codeforces - Educational Round 86
# Problem A - 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(x,y,a,b):
	n = 0
	while True:
		if x == 0 and y == 0:
			break
			
		if x == 0:
			n += y * a
			y = 0
				
		elif y == 0:
			n += x * a
			x = 0
		
		else:		
			if b < a*2:
				mn = min(x, y)
				n += b * mn
					
				x -= mn
				y -= mn
			
			else:
				n += (x+y) * a
				x = 0
				y = 0
				
		#print ("{} {}".format(x,y))
		
	return n


# Main
t = read_int()
for case in range(t):
	x, y = read_ints()
	a, b = read_ints()
	
	sol = solve(x, y, a, b)
	
	print (sol)
