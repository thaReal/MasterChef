#!/usr/bin/python


# Main
n = int(raw_input())
a = [int(x) for x in raw_input().split(" ")]

wildcard = False
sign = 1
coins = 0

for i in a:
	if i < 0:
		sign *= -1
	
	if i == 0:
		wildcard = True
		coins += 1
	else:
		coins += (abs(i) - 1)

if sign == -1 and wildcard == False:
	coins += 2

print coins
