#!/usr/bin/python

# Main
n = int(raw_input())
m = (n / 2) + 1

print m
for i in range(n/2):
	coord = str(i + 1) + " 1"
	print coord
	
for i in range(n/2):
	coord = str(i + 1) + " " + str(m)
	print coord
	
if n % 2 == 1:
	print "%s %s" % (m, m)
