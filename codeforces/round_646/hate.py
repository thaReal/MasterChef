#!/usr/bin/python3

# Codeforces - Round 646
# Author: frostD
# Problem B - Subsequence Hate 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(s):
	l = len(s)
	if l < 3:
		return 0
	
	changes = 0
	groups = make_groups(s)
	lengths = []
	while len(groups) > 2:	
		for g in groups:
			lengths.append(len(g))
		
		min_len = min(lengths)
		selections = []
		for i in range(len(groups)):
			if len(groups[i]) == min_len:
				selection = min_len
				if i != 0:
					selection += len(groups[i-1])
				if i != len(groups) - 1:
					selection += len(groups[i+1])
				selections.append(selection)
			else:
				selections.append(0)
		
		target = max(selections)
		idx = selections.index(target)
		selection = groups[idx]
		c = len(selection)
		
		if '1' in selection:
			selection = '0' * c
		else:
			selection = '1' * c
		
		groups[idx] = selection
		changes += c
		
		s = ''.join(groups)
		groups = make_groups(s)
		lengths = []
		
		#print ("new s: {}".format(s)) # debug
		#print ("changes: {}".format(changes)) # Debug
		
	return changes 
		
		
		
def make_groups(s):
	groups = []
	val = s[0]
	g = s[0]
	for i in range(1, len(s)):
		if s[i] == val:
			g += s[i]
		else:
			groups.append(g)
			g = s[i]
			val = s[i]
	
	groups.append(g) 
	return groups
	


# Main
t = read_int()
for case in range(t):
	s = input()
	sol = solve(s)
	
	print (sol)
