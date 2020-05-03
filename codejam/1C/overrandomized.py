#!/usr/bin/python3
'''
Codejam 2020 - Round 1C
Problem: "Overrandomized"
Author: Daniel Ruland
'''

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
def solve(U, data):
	if U == 2:
			ltr_set = set()
		for i in data:
			li = i[1]
			for l in li:
				ltr_set.add(l)
			if len(ltr_set) == 10:
				break
	
		ltrs = list(ltr_set)
		ltr_dict = {}
		for i in data:
			n = i[0]
			val = i[1][0]
			if val in ltr_dict:
				if n < ltr_dict[val]:
					ltr_dict[val] = n
			else:
				ltr_dict[val] = n
	
		if len(ltr_dict) == 9:
			for k in ltr_dict.keys():
				ltrs.remove(k)
			l0 = list(ltrs)[0]	
		
			ltr_dict[l0] = 0
	
		# final step
		sol = ''
		for i in range(10):
			for k in ltr_dict.keys():
				if ltr_dict[k] == i:
					sol += k
					continue
				
		return sol
	
	else:
		ltr_set = set()
		f_set = set()
		for i in data:
			li = i[1]
			first = li[0]
		
			for l in li:
				ltr_set.add(l)
			f_set.add(first)
		
			if len(ltr_set) == 10 and len(f_set) == 9:
				break
	
		ltr_dict = {}
		ltr_dict[0] = ltr_set.difference(f_set)
		# Now we have 0
		
	
	
		



# Main
T = read_int()
for x in range(T):
	# Solution
	U = read_int()
	data = []
	for i in range(pow(10, 4)):
		val = input().split(" ")
		val[0] = int(val[0])
		data.append(val)
		
	sol = solve(U, data)
	
	# Output
	print ("Case #{}: {}".format(x+1, sol))
