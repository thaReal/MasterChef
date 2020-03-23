#!/usr/bin/python3

# Codeforces - Educational Round 84
# Problem B - Princesses and Princes 


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints


def solve(n):
	princes = set(range(1,n+1))
	matches = []
	princesses = []
	for j in range(n):
		princesses.append(read_ints()[1:])
		matches.append(0)
		for choice in princesses[j]:
			if choice in princes:
				princes.remove(choice)
				matches[j] = 1
				break
			
	if len(princes) == 0:
		return "OPTIMAL"
	
	else:
		prince = list(princes)[0]
		princess = matches.index(0) + 1
		return "IMPROVE\n{} {}".format(princess, prince)
		

# Main
t = read_int()
for i in range(t):
	n = read_int()
		
	print (solve(n))
