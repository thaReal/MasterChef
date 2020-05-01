#!/usr/bin/python3

def binary_search(a, b, include_endpoints=True):
	n_range = abs(b - a)
	direction = 1 #moving in postivie direction
	step = n_range
	
	guess = a
	result = check_guess(guess)
	
	
	
def check_guess(guess):
	'''Template for whatever search / matching / guessing function'''
	pass
	
	


# These functions are all specific to codejam dart throwing game
# Hits and Misses are treated as 1 and 0 respectively

class Tester(object):
	def __init__(self, a, b, value):
		self.a = a
		self.b = b
		self.value = value
		
		self.guess_count = 0
		
	def check_guess(self, guess):
		if guess < a or guess > b:
			print ("[-] Out of bounds error")
		
		self.guess_count += 1		
		if guess >= self.value:
			return 'HIT'
		
		else:
			return 'MISS'
		
		


def binary_search_boundary(a, b, tester):
	''' Binary search for the 'HIT' / 'MISS' boundary between
	a and b. Returns value corresponding to hit side of boundary
	(by the problem definition, the right side)'''
	
	n_range = abs(b - a)
	direction = 1 #moving in postivie direction
	step = n_range
	
	guess = a
	result = tester.check_guess(guess)
	
	# If we get a hit on our first guess, we can't move back any further
	# so that means we're already at the boundary point
	if result == 'HIT':
		return guess

	while step >= 1:
		prev_result = result
		guess = guess + step * direction
		result = tester.check_guess(guess)
		
		if result != prev_result:
			direction = 1 if direction == -1 else -1
		
		step //= 2
	
	# depending where loop exits, we may be on the left side of the boundary
	if result == 'MISS':
		guess += 1
		
	return guess
		
	
if __name__=='__main__':
	a = 1
	b = 10
	value = 6
	
	tester = Tester(a, b, value)
	guess = binary_search_boundary(a, b, tester)
	
	if guess == value:
		result = 'CORRECT'
	else:
		result = 'INCORRECT'
	
	print ("Guess: {}, Value: {} - {}".format(guess, value, result))
	print ("# of Guesses: {}".format(tester.guess_count))
