#!/usr/bin/python

def readline():
	line = [int(x) for x in raw_input().split(" ")]
	return line

#Main
l1 = readline()
h = l1[0]
w = l1[1]

r = readline()
c = readline()

ai = list()
for i in range(h):
	ai.append(['I']*w)

invalid = False

# first input rows
for i in range(h):
	# if row = width, entire row is 1s
	if r[i] == w:
		for j in range(r[i]):
			ai[i][j] = 1
			
	# otherwise 1s up until value, and then a 0
	else:
		for j in range(r[i]):
			ai[i][j] = 1
		ai[i][r[i]] = 0	

# Then input columns, checking for validity
for i in range(w):
	if invalid == True:
		break
	
	# if row = height, entire row is 1s
	if c[i] == h:
		# for each value check to see if it was already set to 0
		for j in range(c[i]):
			if ai[j][i] == 0:
				invalid = True
				break
			ai[j][i] = 1
			
	# otherwise 1s up until value, and then a 0
	else:
		#for each value check to see if was already set to 0
		for j in range(c[i]):
			if ai[j][i] == 0:
				invalid = True
				break
			ai[j][i] = 1
		
		# finally check last value isn't 1 and set to 0
		if ai[c[i]][i] == 1:
			invalid = True
			break
		ai[c[i]][i] = 0	
		
# now we *should* be able to sum the array and find the solution
if invalid:
	print 0
else:
	ic = 0
	for i in range(h):
		for j in range(w):
			if ai[i][j] == 'I':
				ic += 1
	if ic != 0:
		sol = pow(2, ic)
	else:
		# if possible, sol = 1
		sol = 1	
	print sol % 1000000007

