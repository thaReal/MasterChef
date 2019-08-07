#!/usr/bin/python

# Main
n = int(raw_input())
ai = [int(x) for x in raw_input().split(" ")]

sm = 0
for i in range(n):
	sm += ai[i]
	
mx = max(ai)
if mx > (sm - mx):
	print "NO"

elif sm % 2 != 0:
	print "NO"

else:
	print "YES"
