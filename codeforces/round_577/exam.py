#!/usr/bin/python
from collections import Counter

# Main

l1 = [int(x) for x in raw_input().split(" ")]
n = l1[0]
m = l1[1]

answers = list()
for i in range(n):
	answers.append(raw_input())

scores = [int(x) for x in raw_input().split(" ")]

total = 0
for i in range(m):
	cnt = Counter()
	for j in range(n):
		cnt[answers[j][i]] += 1
	
	max_ans = max(cnt.values())
	score = max_ans * scores[i]
	total += score
	
print total
