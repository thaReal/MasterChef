#!/usr/bin/python

# Main
s = raw_input()
n = len(s)

w_ind = []
o_ind = []
for i in range(n):
	char = s[i]
	if char == 'v':
		if i != n-1:
			if s[i+1] == 'v':
				w_ind.append(i)
	else:
		o_ind.append(len(w_ind))

tot = len(w_ind)
wow = 0
for o in o_ind:
	wow += o * (tot - o)
	
print wow
