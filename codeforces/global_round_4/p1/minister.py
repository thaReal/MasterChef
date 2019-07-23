#!/usr/bin/python

# Main

n = int(raw_input())
an = [int(x) for x in raw_input().split(" ")]

tot = sum(an)
alice = an.pop(0)
coalition = [alice]
ci = [1]

for i in range(len(an)):
	if float(an[i]) <= (float(alice) / 2.0):
		coalition.append(an[i])
		ci.append(i+2)
		
ctot = sum(coalition)
if ctot > tot / 2:
	print len(coalition)
	istr = [str(x) for x in ci]
	print " ".join(istr)
else:
	print 0
