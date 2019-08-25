#!/usr/bin/python
from collections import defaultdict


# Main
n = int(raw_input())
a = [int(x) for x in raw_input().split(" ")]

d = defaultdict(int)
first_seen = list()
second_seen = list()

for i in range(n):
	if d.get(a[i]) == None:
		d[a[i]] = i
	else:
		first_seen.append(d[a[i]])
		second_seen.append(i)
		
			
'''	
if l == 0:
	print 0
	
elif r == 0:
	print 1
'''
print first_seen
print second_seen
