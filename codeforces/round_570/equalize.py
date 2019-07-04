#!/usr/bin/python
# Codeforces Round 570 (Div 3)
# Equalize Prices

def equalize(an, k):
	mn = min(an)
	mx = max(an)
	if mx - mn <= 2*k:
		return max(mx - k, mn + k)
	else:
		return -1


#Main
q = int(raw_input())
for query in range(q):
	data = [int(x) for x in raw_input().split(" ")]
	n = data[0]
	k = data[1]
	
	an = [int(x) for x in raw_input().split(" ")]
	sol = equalize(an, k)
	print sol
