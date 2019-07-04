#!/usr/bin/python
good = [4, 8, 15, 16, 23, 42]

def lose_it(data):
	l = len(data)
	stacks = dict()
	for i in range(6):
		stacks[i+1] = 0
	
	for i in data:
		index = good.index(i)
		if index == 0:
			stacks[1] += 1
		else:
			if stacks[index] > 0:
				stacks[index] -= 1
				stacks[index+1] += 1
	
	g = stacks[6] * 6
	return l - g


# Main
n = int(raw_input())
raw_data = raw_input().split(" ")
data = [int(x) for x in raw_data]
	
solution = str(lose_it(data))
print solution
