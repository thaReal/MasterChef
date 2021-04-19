#!/usr/bin/python3      

'''
Codejam 2021 - Round 1A
Problem: "Hacked Exam"
Author: Daniel Ruland
'''

# Utility Functions
def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	
	
# Solution:
def invert(exam):
	inverted = ""
	for char in exam:
		if char == "T":
			inverted += "F"
		else:
			inverted += "T"
	
	return inverted
	

def solve(n, q, exams, scores):
	best = 0
	sol = ''
	for i in range(n):
		if scores[i] > best:
			best = scores[i]
			sol = exams[i]
		
		elif (q - scores[i]) > best:
			best = (q - scores[i])
			sol = invert(exams[i])
			
	if sol == '':
		sol = 'T' * q
	
	return "{} {}/1".format(sol, best)

# Main
T = read_int()
for i in range(T):
	n, q = read_ints()
	exams = []
	scores = []
	for _ in range(n):
		A, S = input().split(" ")
		exams.append(A)
		scores.append(int(S))
    
	sol = solve(n, q, exams, scores)
	
	# Output
	print ("Case #{}: {}".format(i+1, sol))
