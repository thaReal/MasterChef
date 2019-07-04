#!/usr/bin/python

from collections import deque

def operate(d):
	A = d.popleft()
	B = d.popleft()
	if A > B:
		d.appendleft(A)
		d.append(B)
	else:
		d.appendleft(B)
		d.append(A)

# Main
l1 = [int(x) for x in raw_input().split(" ")]
n = l1[0]
q = l1[1]

an = [int(x) for x in raw_input().split(" ")]
d = deque(an)
mx = max(d)

i = 0
phase = list()

while d[0] != mx:
	phase.append(str(d[0]) + " " + str(d[1]))
	operate(d)
	i += 1

lp = len(phase)

cycle = list()
for j in range(n-1):
	cycle.append(str(mx) + " " + str(d[j+1]))
	i += 1

lc = n - 1


for i in range(q):
	qi = int(raw_input())
	if qi <= lp:
		print phase[qi-1]
	else:
		print cycle[((qi - lp) % lc)-1]


