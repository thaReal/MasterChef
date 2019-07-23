#!/usr/bin/python


# works but too slow
def lcs(X, Y, m, n, s=""):
	if len(s) >= mx:
		return(0, s)
	if m == 0 or n == 0:
		return (0, s)
	elif X[m-1] == Y[n-1]:
		s += X[m-1]
		m1 = lcs(X, Y, m-1, n-1, s=s)
		return (1+m1[0], m1[1])
	else:
		m1 = lcs(X, Y, m, n-1, s=s)
		m2 = lcs(X, Y, m-1, n, s=s)
		if m1[0] > m2[0]:
			s = m1[1]
			return (m1[0], s)
		else:
			s = m2[1]
			return (m2[0], s)

			

# Main
s = raw_input()
n = len(s)

r = reversed(s)
sr = ""
for i in r:
	sr += i

global mx
mx = (n/2) + 1

print lcs(s, sr, n, n)[1]
