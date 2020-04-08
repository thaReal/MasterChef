#!/usr/bin/python3
'''
Codejam 2020 Qualification Round 
Problem: "Nesting Depth"
Author: Daniel Ruland
'''

def read_int():
	n = int(input())
	return n


# Main
t = read_int()
case = 1
for x in range(t):
	s = input()
	
	sol = ''
	clvl = 0	
	for i in s:
		nlvl = int(i)
		while clvl != nlvl:
			if clvl < nlvl:
				sol += '('
				clvl += 1
			
			elif clvl > nlvl:
				sol += ')'
				clvl -= 1
		
		sol += i
	
	while clvl != 0:
		sol += ')'
		clvl -= 1
	
	# Output
	print ("Case #{}: {}".format(x+1, sol))
	case += 1
