#!/usr/bin/python3

# Codeforces - Round 636
# Problem D - Constant Palindrome Sum

from collections import Counter

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def solve(n,k,a):
	cntr = Counter()
	for i in range(n // 2):
		cntr[a[i] + a[n-i-1]] += 1
	
	mx = max(cntr.values())
	sums = []
	for elem in cntr:
		if cntr[elem] == mx:
			sums.append(elem)
	
	#print (sums)
	target = min(sums)
	#print ("target: {}".format(target)) #debug
	
	sol = 0
	for i in range(n // 2):
		sm = a[i] + a[n-i-1]
		if sm == target:
			continue
			
		elif sm > target and min(a[i], a[n-i-1]) > target:
			sol += 2
			#print ('+2') #debug	
		
		elif sm < target and max(a[i], a[n-i-1]) + k  < target:  
			sol += 2
			#print ('+2') #debug
			
		else:
			sol += 1
			#print ('+1') #debug
	
	# I knew this wasn't valid - more of a "buzzer shot" situation
	if sol > n//2:
		sol = n// 2
				
	return sol

# Main
t = read_int()
for case in range(t):
	n, k = read_ints()
	a = read_ints()
	sol = solve(n, k, a)
	
	print (sol)
