#!/usr/bin/python
from collections import defaultdict


# Main
n = int(raw_input())
a = [int(x) for x in raw_input().split(" ")]
sol = None

cnt = defaultdict(int)
for i in a:
	cnt[i] += 1


if cnt[0] > 1:
	sol = "cslnb"
else:
	for i in cnt.keys():
		if cnt[i] > 2:
			sol = "cslnb"
			break
		
			
