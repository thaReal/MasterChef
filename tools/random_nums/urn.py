#!/usr/bin/python3

import random
from bisect import bisect
from itertools import accumulate


def urn_problem(population, weights, k):
	'''Given a population and a weighted distribution, will return k samples
	*without replacement*. For the example problem there are three colored 
	balls, with the weights representing the count of each ball respectively.
	k is the number of balls we wish to remove from the urn'''
	
	cum_weights = list(accumulate(weights))
	total = cum_weights.pop()
	selections = random.sample(range(total), k=k)
	
	indices = [bisect(cum_weights, s) for s in selections]
	result = [population[i] for i in indices]
	
	return result


def test_urn_problem():
	population = ['red', 'blue', 'green']
	weights = [10, 4, 18]
	k = 9
	
	res = urn_problem(population, weights, k)
	print (res)


#-----

	
def weighted_selection(population, weights):
	'''Similiar to urn problem however this function is designed for a single
	selection. This allows for generating a weighted distribution *with
	replacement* by looping this function k times as required'''
	
	cum_weight = list(accumulate(weights))
	total = cum_weight.pop()
	selection = random.sample(range(total), k=1)
	
	idx = [bisect(cum_weight, s) for s in selection]
	result = [population[i] for i in idx][0]
	
	return result



def test_weighted_selection():
	population = [0, 1]
	weights = [1, 3]
	res = weighted_selection(population, weights)
	print (res)
	

#-----


def weighted_selection_replacement(weights, k):
	'''Implementation of above function to provide k elements from
	a weighted population distribution *with replacement*'''
	
	n = len(weights)
	population = list(range(n))
	res = []
	for i in range(k):
		elem = weighted_selection(population, weights)
		res.append(elem)
	
	return res
	
	
def test_weighted_selection_replacement():
	weights = [1,3]
	k = 5
	res = weighted_selection_replacement(weights, k)
	
	print (res)
	
	
	
	
if __name__=='__main__':
	#test_urn_problem()
	#test_weighted_selection()
	test_weighted_selection_replacement()
	
