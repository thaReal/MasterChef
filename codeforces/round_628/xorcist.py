#!/usr/bin/python3

# Codeforces - Round 628
# Problem D - Ehab the Xorcist 


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def xor_set(n):
	vn = set()
	a = 0
	while a <= n:
		vn.add(a^n)
		a += 1
		n -= 1

	return vn
	

# Main
line = read_ints()
u = line[0]
v = line[1]

if u > v:
	print (-1)
	
elif u == v:
	if v == 0:
		print 0
	else:
		pass
		
# INCOMPLETE - Possibly attempt recursive calls to xor_set on v until a 
# value matching u can be achieved, otherwise return -1
	
