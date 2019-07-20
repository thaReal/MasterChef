#!/usr/bin/python





# Main
a = raw_input()
b = raw_input()
 
lb = len(b)
l = len(a) - lb + 1
cntb = b.count('1')
 
cnt = 0
for i in range(l):
	
	ai = int(a[i:i+lb], base=2)
	print a[i:i+lb] + ": " + str(ai)
	
	'''
	res = ai ^ bi
	bc = bin(res).count('1') #bitcount
	if bc % 2 == 0:
	'''
	if ai % 2 == bi % 2:	
		cnt += 1
 
print cnt
