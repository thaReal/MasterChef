#!/usr/bin/python3

'''
Kickstart 2021 - Round B 
Problem: "Consecutive Primes"
Author: Daniel Ruland
'''

# Utility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints


def SieveOfEratosthenes(n):
	if n == 0:
		return 0
		
	prime = [True for i in range(n + 1)] 
	p = 2
	while (p * p <= n): 
		# If prime[p] is not changed, then it is a prime 
		if (prime[p] == True): 
			
			# Update all multiples of p 
			for i in range(p * 2, n + 1, p): 
				prime[i] = False
		p += 1
		
	prime[0]= False
	prime[1]= False
	
	# Print all prime numbers
	primes = []
	for p in range(n): 
		if prime[p]: 
			primes.append(p)
	
	return primes
	
# Solution:
def solve(z, primes):
	Rj = primes[0] * primes[1]
	i = 1
	while Rj <= z:
		Ri = Rj
		Rj = primes[i] * primes[i+1]
		i += 1
	
	return Ri
	

# Main
t = read_int()
primes = SieveOfEratosthenes(50000)
for i in range(t):
	# Solution
	z = read_int()
	sol = solve(z, primes)
	
	# Output
	print ("Case #{}: {}".format(i+1, sol))
