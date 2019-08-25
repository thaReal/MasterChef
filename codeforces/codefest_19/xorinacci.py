#!/usr/bin/python



# Main
t = int(raw_input())

for i in range(t):
	data = [int(x) for x in raw_input().split(" ")]
	a = data[0]
	b = data[1]
	n = data[2]

	fn = [a, b]
	fn.append(a ^ b)
	ind = n % 3
	
	print fn[ind]
