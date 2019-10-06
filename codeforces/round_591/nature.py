#!/usr/bin/python

def readline():
	data = [int(x) for x in raw_input().split(" ")]
	return data

#Main
q = int(raw_input())
for i in range(q):
	n = int(raw_input())
	p = readline()
	
	xa = readline()
	yb = readline()
	
	k = int(raw_input())
	
	x = xa[0]
	a = xa[1]
	y = yb[0]
	b = yb[1]
	
	#contribution list
	cl = list()
	for j in range(n):
		cont = 0
		if (j+1) % a == 0:
			cont += x
			
		if (j+1) % b == 0:
			cont += y
		cl.append(cont)
	
	p.sort(reverse=True)
	
	sol = -1
	for j in range(n):
		cont = 0
		conts = cl[:(n-j)]
		conts.sort(reverse=True)
		prices = p[:(n-j)]
		for ji in range(n-j):
			cont += (prices[ji] / 100) * conts[ji]
		
		if cont < k:
			break
		else:
			sol = n-j
	
	print sol
		
		
