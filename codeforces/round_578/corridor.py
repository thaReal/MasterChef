#!/usr/bin/python
from math import gcd

# Main
l1 = [int(x) for x in raw_input().split(" ")]
n = l1[0]
m = l1[1]
q = l1[2]

com_lines = [(0,0)]
wall_space_i = 360.0 / float(n)
wall_space_o = 360.0 / float(n)



for i in range(q):
	qi = [int(x) for x in raw_input().split(" ")]
	sx = qi[0]
	sy = qi[1]
	ex = qi[2]
	ey = qi[3]


