#!/usr/bin/python3
# Problem: Even but not Even
# Codeforces Round #616 - Danny Ruland

def ebne(n):
	s = str(n)
	
	if len(s) == 1:
		return -1	
	else:
		while int(s[-1]) % 2 == 0:
			s = s[:-1]
			if len(s) == 1:
				return -1

	if sum([int(x) for x in s]) % 2 == 0:
		return int(s)
		
	else:
		for i in range(len(s) - 1):
			ind = len(s) - i - 2
			if int(s[ind]) % 2 == 1:
				 return s[:ind] + s[ind+1:]

	return -1

# Main
t = int(input())
for i in range(t):
	l = int(input())
	n = int(input())
	sol = ebne(n)
	print(sol)
