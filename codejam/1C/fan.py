#!/usr/bin/python3
'''
Codejam 2020 - Round 1C
Problem: "Overexcited Fan"
Author: Daniel Ruland
'''

def read_int():
	n = int(input())
	return n

	
def move(x,y,m,i):
	if m[i] == 'N':
		return x, y+1
		
	if m[i] == 'S':
		return x, y-1
	
	if m[i] == 'E':
		return x+1, y
	
	if m[i] == 'W':
		return x-1, y
	
	
def solve(x,y,m):
	locn = [(x,y)]
	n = len(m)
	for i in range(n):
		x, y = move(x,y,m,i)
		locn.append((x,y))
		
	t_list = []
	for i in range(len(locn)):
		t = abs(locn[i][0]) + abs(locn[i][1])
		t_list.append(t)
	
	#print (locn) #Debug
	#print (t_list) #Debug
	
	for t in range(len(t_list)):
		tm = t_list[t]
		if t >= tm:
			return t
	
	return 'IMPOSSIBLE'
	
	


# Main
T = read_int()
for i in range(T):
	X, Y, M = input().split(" ")
	x = int(X)
	y = int(Y)
	m = [l for l in M]
	
	sol = solve(x,y,m)
	
	# Output
	print ("Case #{}: {}".format(i+1, sol))
