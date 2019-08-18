#!/usr/bin/python

# Main
n = int(raw_input())
a = [int(x) for x in raw_input().split(" ")]
m = int(raw_input())
b = [int(x) for x in raw_input().split(" ")]


def choose_two(a, b):
	s = set(a+b)
	for i in a:
		for j in b:
			found = False
			for k in s:
				if i + j == k:
					found = True
			if found == False:
				return i, j
				
				
i, j = choose_two(a, b)
print str(i) + " " + str(j)
