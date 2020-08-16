#!/usr/bin/python3

# Codeforces - Global Round 10
# Author: frostD
# Problem D - Omkar and Bed Wars 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n, s):
	wrong = [0 for x in range(n)]
	for i in range(0, n, 2):
		if len(set(s[i:i+2])) == 1:
			wrong[i] = wrong[i] ^ 1
			try:
				wrong[i+1] = wrong[i+1] ^ 1
			except:
				continue
	
	return wrong

'''
def solve(n, s):
	# Lets first check and see which players are playing "wrong"
	wrong = [0 for x in range(n)]
	for i in range(n):
		right = 0
		left = 0
		
		if i == 0:
			if s[-1] == 'R':
				left = 1
		else:
			if s[i-1] == 'R':
				left = 1
				
		if i == n-1:
			if s[0] == 'L':
				right = 1
		else:
			if s[i+1] == 'L':
				right = 1
		
		cnt = left + right
		
		if cnt == 2 or cnt == 0:
			continue
		
		if left and s[i] == 'R':
			wrong[i] = 1
		
		if right and s[i] == 'L':
			wrong[i] = 1
	
	# Now that we have the 'wrong' array, calculate how many talks he needs to fix it
	talks = 0
	while 1 in wrong:
		if n % 2 == 1 and wrong.count(1) == 1:
			break
		
		idx = wrong.index(1)
		if idx == 0:
			if wrong[-1] == 1:
				wrong[0] = 0
				wrong[-1] = 0
				talks += 1
							
			elif wrong[idx+1] == 1:
				wrong[0] = 0
				wrong[idx+1] = 0
				talks += 1
				
		else:
			if idx == n-1:
				wrong[idx] = 0
				talks += 1
				
			elif wrong[idx+1] == 1:
				wrong[idx] = 0
				wrong[idx+1] = 0
				talks += 1
			
			else:
				wrong[idx] = 0
				talks += 1
			
	return talks
'''
		
	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	s = input()
	
	sol = solve(n, s)
	print (sol)
