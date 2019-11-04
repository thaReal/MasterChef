#!/usr/bin/python


# Main
line = [int(x) for x in raw_input().split(" ")]
a = line[0]
b = line[1]

if b - a == 1:
	print "%s %s" % (a, b)

elif b - a == 0:
	print str(a) + "0 " + str(b) + "1"
	
elif a == 9 and b == 1:
	print "99 100"

else:
	print "-1"
