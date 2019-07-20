#!/usr/bin/python


# Main
data = [int(x) for x in raw_input().split(" ")]
n = data[0]
m = data[1]
k = data[2]

if m >= n and k >= n:
	print "Yes"
else:
	print "No"
