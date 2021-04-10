#!/usr/bin/python3      

'''
Codejam 2021 Qualification Round - Practice
Problem: "Median Sort"
Author: Daniel Ruland
'''
import sys

# -----------------
# Utility Functions
# -----------------

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints


# ---------------------
# Interaction Functions
# ---------------------

def query_judge(x1, x2, x3):
	print("{} {} {}".format(x1, x2, x3))
	sys.stdout.flush()

	response = read_int()
	if response == -1:
		sys.exit(-1)
	
	return response
	

def submit_answer(sol):
	#logfile.write("Submitting: {}\n".format(' '.join([str(x) for x in sol])))
	print(' '.join([str(x) for x in sol]))
	sys.stdout.flush()
	
	response = read_int()
	
	if response == 1:
		#logfile.write("[+] Answer Correct!\n\n")
		return
		
	if response == -1:
		#logfile.write("[-] Incorrect answer, exiting\n")
		sys.exit(-1)
	
	
	
# --------
# Solution
# --------

def init():
	median = query_judge(1, 2, 3)
	s = set([1, 2, 3])
	s.remove(median)
	l = list(s)

	return [l[0], median, l[1]] 


def search_index(sol, i):
	n = len(sol)
	li = 0
	ri = n-1
	
	#logfile.write("Searching for: {}\n\n".format(i))
	#logfile.write("li:{}, ri: {}, query: {}\n".format(li, ri, [i, sol[li], sol[ri]]))
	idx = query_judge(i, sol[li], sol[ri])
	
	#logfile.write("response: {}\n".format(idx))
	
	if idx == sol[li]:
		#logfile.write("i: {}, index: {}\n".format(i, idx))
		return 0
	
	if idx == sol[ri]:
		#logfile.write("i: {}, index: {}\n".format(i, idx))
		return n
	
	while li + 1 < ri:
		guess = ((ri - li) // 2) + li
		#logfile.write("li:{}, ri: {}, query: {}\n".format(li, ri, [i, sol[guess], sol[ri]]))
		
		median = query_judge(i, sol[guess], sol[ri])
		#logfile.write("response: {}\n".format(median))
		
		if median == i:
			li = guess
		
		else:
			ri = guess
	
	return ri
	
	
def insert_val(sol, idx, i):
	n = len(sol)
	if idx == 0:
		return [i] + sol

	if idx == n:
		return sol + [i]
		
	return sol[:idx] + [i] + sol[idx:]
	

def solve(N, Q):
	sol = init()
	
	#logfile.write("init solution: {}\n".format(sol))
	
	for i in range(4, N+1):
		idx = search_index(sol, i)
		sol = insert_val(sol, idx, i)
		#logfile.write("Found - idx: {}, sol: {}\n\n".format(idx, sol))
	
	submit_answer(sol)
	
# ----	
# Main
# ----



T, N, Q = read_ints()

#logfile = open('logfile.txt', 'w')
#logfile.write("T: {}, N:{}, Q: {}\n".format(T, N, Q))

for i in range(T):
    solve(N, Q)

#logfile.close()
sys.exit(0)
    
    
    
	
