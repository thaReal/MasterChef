#!/usr/bin/python

# Main
x = int(raw_input())
hp = x % 4

if hp == 1:
	print "0 A"
elif hp == 2:
	print "1 B"
elif hp == 3:
	print "2 A"
else:
	print "1 A"

