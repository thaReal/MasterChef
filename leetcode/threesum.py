#!/usr/bin/python3

# Leetcode #15 - 3Sum

def threeSum(nums):
	lindex = 0
	rindex = len(nums) - 1
	sol = []
	
	while lindex < rindex:
		ln = nums[lindex]
		rn = nums[rindex]
		
		found = False
		for i in range(lindex+1, rindex):
			if ln + rn + nums[i] == 0:
				cand = [ln, rn, nums[i]]
				cand.sort()
				sol.append(cand)
				found = True
				break
			
		if found:
			lindex += 1
		else:
			rindex -= 1
			
	new_sol = []
	for i in sol:
		if i not in new_sol:
			new_sol.append(i)
	
	return new_sol

if __name__=='__main__':
	nums = [int(x) for x in input("> ").split(" ")]
	sol = threeSum(nums)
	print (sol)
