#!/usr/bin/python3

# seive_of_eratosthenes.py: Danny Ruland 
# Description: Seive of Eratosthenes implementation to calculate all the prime 
# numbers less than or equal to n 

'''
Create a boolean array "prime[0..n]" and initialize 
all entries it as true. A value in prime[i] will 
finally be false if i is Not a prime, else true. 
'''

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
			
			

# driver program 
if __name__=='__main__': 
	n = 100000000
	primes = SieveOfEratosthenes(n)
	#print (primes)
	print (primes[-1] * primes[-2])
	if primes[-1] * primes[-2] > 10 ** 18:
		print (primes[-1] * primes[-2] - 10**18)
	
	else:
		print ("Boo")
	
	#n = 999999733 #too big

