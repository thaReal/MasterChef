#!/usr/bin/python3

# Codeforces - Round 619
# Problem #2 - Motarack's Birthday

t = int(input())
for case in range(t):
	n = int(input())
	a = [int(x) for x in input().split(" ")]
	ai = []
	
	# First strip out duplicate '-1' values
	prev_m = False
	for val in a:
		if val == -1:
			if prev_m == False:
				prev_m = True
				ai.append(val)
		else:
			prev_m == False
			ai.append(val)
	
	# then do one more pass and adjust min value and diff
	# at each mising location
	k_min = 0
	d_min = 0
	for i in range(len(ai)):
		if ai[i] == -1:
			# special cases for first index
			if i == 0:
				k_min = ai[i]
				k_min = 0
				continue
			
			# and special case for the last index
			if i == len(ai) - 1:
				d = abs(k_min - ai[-2])
			
			# otherwise compute d from adjacent values
			else:
				d = abs(
				
			k_min =
				
			
				
			
