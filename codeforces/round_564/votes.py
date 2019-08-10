#!/usr/bin/python

# Main
data = [int(x) for x in raw_input().split(" ")]

x = data[0]
y = data[1]
z = data[2]

if x > y + z:
	print "+"
elif y > x + z:
	print "-"
elif z == 0 and x == y:
	print "0"
else:
	print "?"
