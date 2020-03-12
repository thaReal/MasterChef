#!/usr/bin/python3

# Codeforces - Codecraft 20
# Problem B - String Modification 

# not working, seems like I'm pretty damn close


def modify(s, k):
	for i in range(len(s) - k + 1):
		lb = i
		rb = i+k
		s = s[:lb] + s[lb:rb][::-1] + s[rb:]
	
	return s


# Main
t = int(input())
for case in range(t):
	n = int(input())
	s = input()
		
	mn = min(s)
	if s.count(mn) == 1:
		k = s.index(mn) + 1
		s = modify(s, k)
		print (s)
		print (k)

	else:
		l1 = []
		l2 = []
		for i in range(len(s)):
			if s[i] == mn:
				k = i + 1
				sn = s[1:k][::-1] + s[k:]
				l1.append(k)
				l2.append(sn)
				
		idx = l2.index(min(l2))
		k = l1[idx]		
		smin = modify(s, k)
		
		print (smin)
		print (k)
