#!/usr/bin/python


#Main
data = [int(x) for x in raw_input().split(" ")]
l = data[0]
r = data[1]

sol = -1

for i in range(l,r+1):
	s = str(i)
	if len(set(s)) == len(s):
		sol = i
		break

print sol
