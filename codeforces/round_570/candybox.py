#!/usr/bin/python
# Codeforces Round 570 (Div 3)
# Computer Game

from collections import defaultdict

# too slow
def candysort(n, an):
	box = defaultdict(int)
	for ai in an:
		box[ai] += 1
	
	candies = box.values()
	candies.sort(reverse=True)

	for i in range(len(candies)):
		if i == 0:
			val = candies[i]
			continue
			
		if val == 1:
			candies = candies[:i]
			break
		
		if candies[i] >= val:
			candies[i] = val - 1
			val = candies[i]
			continue
		
		val = candies[i]

	return sum(candies)


#Main
q = int(raw_input())
for query in range(q):
	n = int(raw_input())
	an = [int(x) for x in raw_input().split(" ")]
	
	sol = candysort(n, an)
	print sol
