#!/usr/bin/python3

# Codeforces - Round 620
# Problem B - Longest Palindrome 

from collections import deque

# Main
data1 = [int(x) for x in input().split(" ")]
n = data1[0]
m = data1[1]

strings = []
for line in range(n):
	strings.append(input())
	

comps = []
singles = []
while len(strings) > 0:
	found = False
	s = strings[-1]
	for i in range(len(strings) - 1):
		if strings[i] == s[::-1]:
			s0 = strings[-1]
			s1 = strings.pop(i)
			comps.append((s0, s1))
			found = True
			break
	
	if found == False:
		if s == s[::-1]:
			singles.append(s)
	
	strings.pop(-1)
	
# Debug	
# print ("comps: {}".format(comps))
# print ("singles: {}".format(singles))

d = deque()
if len(singles) > 0:
	d.append(singles[0])

for c in comps:
	d.appendleft(c[0])
	d.append(c[1])

sol = "".join(d)
l = len(sol)

print (l)
print (sol)
