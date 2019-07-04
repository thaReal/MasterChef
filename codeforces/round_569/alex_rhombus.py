#!/usr/bin/python

def rhombus(n):
	A = 1
	for i in range(n - 1):
		A += (i + 1) * 4
	return A

# Main loop
n = int(raw_input())
print rhombus(n)
