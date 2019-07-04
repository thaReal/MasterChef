#!/usr/bin/python
# Codeforces Round 570 (Div 3)
# Computer Game

def compute(k,n,a,b):
	cs = a - b # charge save: the amount we save by charging
	if n * a < k:
		return n
	
	bn = (n * a) - k + 1 # battery needed
	if cs * n < bn:
		return -1
		
	tc = bn / cs # turns charging
	if bn % cs != 0:
		tc += 1
	
	return n - tc


# Main
q = int(raw_input())
for query in range(q):
	data = [int(x) for x in raw_input().split(" ")]
	k = data[0] # initial charge
	n = data[1] # number of turns
	a = data[2]
	b = data[3]
	
	sol = compute(k,n,a,b)
	print sol
