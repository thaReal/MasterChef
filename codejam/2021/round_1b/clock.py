#!/usr/bin/python3      

'''
Codejam 2021 - Round 1B
Problem: "Broken Clock"
Author: Daniel Ruland
'''
from math import floor

# Utility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
# Solution:
def check(da, db, dc):
	h, rem = deg2hrs(da)
	m, rem2 = deg2mins(db)
	
	if m != rem:
		#print ("m: {}, h: {}".format(m, h))
		return False
		
	s, rem3 = deg2mins(dc)
	
	if s != rem2:
		return False
	
	return (h, m, s)

	
def deg2hrs(t):
	hrs = (t / 360) * 12
	rem = round(hrs - floor(hrs), 6)
	return int(floor(hrs)), int(rem * 60)
	
	
def deg2mins(d):
	mins = (d / 360) * 60
	rem = round(mins - floor(mins), 6)
	return int(floor(mins)), int(rem * 60)
	
	
def solve(a, b, c):
	da = round((a*10**-10) / 12, 9)
	db = round((b*10**-10) / 12, 9)
	dc = round((c*10**-10) / 12, 9)
	
	#print("da: {}, db: {}, dc: {}".format(da, db, dc))
	
	sol = check(da, db, dc)
	if sol:
		return "{} {} {} 0".format(sol[0], sol[1], sol[2])
		
	sol = check(da, dc, db)
	if sol:
		return "{} {} {} 0".format(sol[0], sol[1], sol[2])

	sol = check(db, da, dc)
	if sol:
		return "{} {} {} 0".format(sol[0], sol[1], sol[2])
	
	sol =  check(db, dc, da)
	if sol:
		return "{} {} {} 0".format(sol[0], sol[1], sol[2])
		
	sol = check(dc, da, db)
	if sol:
		return "{} {} {} 0".format(sol[0], sol[1], sol[2])
		
	sol = check(dc, db, da)
	if sol:
		return "{} {} {} 0".format(sol[0], sol[1], sol[2])

	

# Main
T = read_int()
for i in range(T):
    a, b, c = read_ints()
    sol = solve(a, b, c)
	
	# Output
    print ("Case #{}: {}".format(i+1, sol))
