#!/usr/bin/python

letters = "abcdefghijklmnopqrstuvwxyz"
ld = dict()
for i in range(26):
	ld[letters[i]] = []

# Main

n = int(raw_input())
s = raw_input()

for i in range(n):
	char = s[i]
	ld[char].append(i)


m = int(raw_input())
for q in range(m):
	qs = raw_input()
	
	qd = dict()
	for i in range(26):
		qd[letters[i]] = 0
	
	for char in qs:
		qd[char] += 1
	
	for k in qd.keys():
		if qd[k] == 0:
			qd.pop(k)
	
	mx = 0
	for k in qd.keys():
		ind = ld[k][qd[k]-1]
		mx = max(mx, ind+1)

	print mx	
