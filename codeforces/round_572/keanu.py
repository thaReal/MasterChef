#!/usr/bin/python

def check_string(s):
	zero = 0
	one = 0
	for i in s:
		if i == "0":
			zero += 1
		else:
			one += 1
			
	if zero != one:
		return True
	else:
		return False


# Main
n = int(raw_input())
s = raw_input()
valid = check_string(s)
if valid:
	print 1
	print s
	
else:
	print "2"
	l = len(s) - 1
	print s[0:l] + " " + s[l]
