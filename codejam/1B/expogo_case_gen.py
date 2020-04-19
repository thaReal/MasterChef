#!/usr/bin/python

f = open('gen_input-1', 'w')
x = -4
n = 0
for i in range(9):
	y = -4	
	for j in range(9):
		f.write("{} {}\n".format(x, y))
		y += 1
		n += 1
	x += 1
f.write("{}".format(n))
f.close()
