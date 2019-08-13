#!/usr/bin/python


# Main
t = int(raw_input())
ans = []

for i in range(t):
	data = [int(x) for x in raw_input().split(" ")]
	n = data[0]
	m = data[1]
	k = data[2]
	
	game = [int(x) for x in raw_input().split(" ")]
	pos = 0
	sol = "YES"
	
	while pos < n-1:
		h = game[pos]
		h1 = game[pos+1]
	
		delta = abs(h - h1)
		
		if h < h1:
			if delta <= k:
				if k - delta <= h:
					m += k - delta
				else:
					m += h
				pos += 1
				
			else:
				if (k + m) - delta >= 0:
					m -= delta - k
					pos += 1
				else:
					sol = "NO"
					break
		else:
			if delta + k <= h:
				m += delta + k
			else:
				m += h
			pos += 1
	ans.append(sol)

for a in ans:
	print a
