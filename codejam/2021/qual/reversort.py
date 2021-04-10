#!/usr/bin/python3      

'''
Codejam 2021 Qualification Round
Problem: "Reversort"
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
def solve(n, l):
    ret = 0
    for i in range(n-1):
        ji = min(l[i:])
        j = l.index(ji)
        ret += j - i + 1
        
        l = l[:i] + l[i:j+1][::-1] + l[j+1:]
        
    return ret    
	

# Main
T = read_int()
for i in range(T):
    n = read_int()
    l = read_ints()
    sol = solve(n, l)
	
	# Output
    print ("Case #{}: {}".format(i+1, sol))
