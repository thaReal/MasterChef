#!/usr/bin/python3

import random

# These functions are all specific to codejam dart throwing game
# -> Modified version of a binary search looking to determine the boundary
# between 'HIT' and 'MISS' return values

class Tester(object):
	def __init__(self, a, b, value):
		self.a = a
		self.b = b
		self.value = value
		
		self.guess_count = 0
		
	def check(self, guess):
		if guess < self.a or guess > self.b:
			print ("[-] Out of bounds error")
		
		self.guess_count += 1		
		if guess >= self.value:
			print ("Guess: {}, Value: {} - HIT".format(guess, self.value))
			return 'HIT'
		
		else:
			print ("Guess: {}, Value: {} - MISS".format(guess, self.value))
			return 'MISS'
	
	
		
# -----

def boundary_search(a, b, tester):	
	guess = a
	result = tester.check(guess)
	if result == 'HIT':
		return guess
	else:
		li = a
	
	guess = b
	result = tester.check(guess)
	if result == 'MISS':
		return -1
	else:
		ri = b
		
	step = abs(b - a)
	direction = -1
	while ri - li > 1:
		if step % 2 == 1:
			step = (step // 2) + 1
		else:
			step //= 2
			
		print ("step: {}".format(step))
		if direction == -1:
			guess = ri - step
		else:
			guess = li + step
		
		result = tester.check(guess)
		if result == 'HIT':
			ri = guess
		else:
			li = guess
		
		direction *= -1
		
	return ri			



def find_cp(x1, y1, x2, y2, r):
	q = sqrt(pow(x2-x1, 2) - pow(y2-y1, 2))
	x3 = (x1 + x2) / 2
	y3 = (y1 + y2) / 2
	
	x = x3 - sqrt(pow(r, 2) - pow((q/2), 2) * (y1-y2) / q)
	y = y3 - sqrt(pow(r, 2) - pow((q/2), 2) * (x2-x1) / q)  
	
	return (x, y)




def directional_boundary_search(a, b, tester):
	'''Similiar to binary boundary search, however only steps from start
	point. Faster when target is expected closer to beginning of range'''
	guess = a
	result = tester.check(guess)
	if result == 'MISS':
		return guess
	else:
		li = a
	
	
		
#------------------#
# Driver Functions #
#------------------#

def boundary_search_driver():
	a = 0
	b = 5400
	
	r = random.Random()
	value = r.randint(a,b)
	#value = 2
	
	tester = Tester(a, b, value)
	guess = boundary_search(a, b, tester)
	
	if guess == value:
		result = 'CORRECT'
	else:
		result = 'INCORRECT'
	
	print ("\nGuess: {}, Value: {} - {}".format(guess, value, result))
	print ("# of Guesses: {}".format(tester.guess_count))
		
#------		
# Main
#------
	
if __name__=='__main__':
	boundary_search_driver()
	
