#!/usr/bin/python

T = int(raw_input())
for q in range(T):
	data = [int(x) for x in raw_input().split(" ")]
	n = data[0] # number of eggs
	s = data[1] # number of stickers
	t = data[2] # number of toys
	
	b = (s + t) - n
	sol = max(s, t) - b + 1
	print sol	
