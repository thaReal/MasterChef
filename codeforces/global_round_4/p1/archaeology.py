#!/usr/bin/python

from collections import deque
from copy import copy

# Main
s = raw_input()

i = 0
j = len(s) - 1
A = deque()

while j-i >= 3:
	if s[i] == s[j]:
		A.append(s[i])
		i += 1
		j -= 1
		
	elif s[i] == s[j-1]:
		A.append(s[i])
		i += 1
		j -= 2
		
	else:
		A.append(s[i+1])
		if s[i+1] == s[j]:
			j -= 1
		else:
			j -= 2
		i += 2

B = copy(A)
B.reverse()

if j >= i:
	A += s[i]
	
print "".join(A) + "".join(B)
