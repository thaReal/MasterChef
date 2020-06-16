#!/usr/bin/python3

'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''


# Main Function
# !-

def climbStairs(n, debug=False):
	# this is the dp array:
	steps = [1,2]
	
	while n > len(steps):
		val = steps[-2] + steps[-1]
		steps.append(val)
	
	if debug:
		print (steps)
		print ('')
		
	return steps[n-1]
	
# Test Cases
# !-

n = 2
sol = climbStairs(n)
print (sol)
# Output: 2

n = 3
sol = climbStairs(n)
print (sol)
# Output: 3

n = 10
sol = climbStairs(n, debug=True)
print (sol)
# Output: 8
