#!/usr/bin/python3

# Codeforces - Round 645
# Author: frostD
# Problem D - The Best Vacation


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, x, d):
	hug_map = []
	for i in range(n):
		vacation = [d[i]]
		while sum(vacation[1:]) < x-1:
			i += 1
			vacation.append(d[i%n])
		
		diff = sum(vacation[1:]) - x - 1
		print ("diff: {}".format(diff))
		if diff > 0:
			if vacation[-1] > vacation[0]:
				hugs = sum(range(vacation[-1] - diff + 1, vacation[-1] + 1))
				hugs += sum(range(vacation[0] - diff + 1))
				for month in vacation[1:-1]:
					hugs += sum(range(month + 1))
			else:
				hugs = vacation[0]
				for month in vacation[1:]:
					hugs += sum(range(month + 1))
		else:
			vacation[-1] += diff
			print ("vacation: {}".format(vacation))
			hugs = vacation[0]
			for month in vacation[1:]:
				hugs += sum(range(month + 1))
		
		hug_map.append(hugs)
	
	if x < max(d):
		dmax = max(d)
		hug_map.append(sum(range(dmax-x+1, dmax+1)))
		
	print (hug_map)
	
	return max(hug_map)
	


# Main
n, x = read_ints()
d = read_ints()
sol = solve(n, x, d)
	
print (sol)
