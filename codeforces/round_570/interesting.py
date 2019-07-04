#!/usr/bin/python
# Codeforces Round 570 (Div 3)
# Nearest Interesting Number


#Main
a = raw_input()
num = int(a)
digits = [int(x) for x in a]

s = sum(digits)

while s % 4 != 0:
	num += 1
	digits = [int(x) for x in str(num)]
	s = sum(digits)

print num
