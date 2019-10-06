#!/usr/bin/python

#Main
q = int(raw_input())
for i in range(q):
	s = raw_input()
	t = raw_input()
	
	ss = set(s)
	st = set(t)
	i = ss.intersection(st)
	
	if len(i) > 0:
		print "YES"
	else:
		print "NO"
