#!/usr/bin/python3

# Codeforces - Round 624
# Problem C - Perform the Combo

from collections import Counter

letters = "abcdefghijklmnopqrstuvwxyz"

def combo(m, s, p):
	cnt = Counter(s)
	ind = 0
	
	p.sort()
	l = len(p)
	
	for i in range(l):
		if p[i] == ind:
			continue
					
		presses = s[ind:p[i]]
		for press in presses:
			cnt[press] += l - i
		ind = p[i]
	
	sol = [str(cnt[l]) for l in letters]
	return " ".join(sol)
		
			
# Main
t = int(input())
for case in range(t):
	nm = [int(x) for x in input().split(" ")]
	n = nm[0]
	m = nm[1]
	s = input()
	p = [int(x) for x in input().split(" ")]
	
	sol = combo(m, s, p)
	print (sol)
