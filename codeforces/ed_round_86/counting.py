#!/usr/bin/python3

# Codeforces - Educational Round 86
# Problem C - Yet Another Counting Problem 


def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

# too slow, need to use mathmatical identity
'''
def solve(a, b, l, r):
	mn = min(l)
	mx = max(r)
	count_map = []
	for i in range(mn, mx+1):
		if i % a % b != i % b % a:
			count_map.append(1)
		else:
			count_map.append(0)
	
	#print (count_map)
	
	sol = []
	for i in range(len(l)):
		li = l[i] - mn
		ri = r[i] - mn + 1
		cnt = sum(count_map[li:ri])
		sol.append(str(cnt))
	
	return ' '.join(sol)
'''
	
def solve(a, b, l, r):
	offset = 0
	i = 0
	while i % a % b == i % b % a:
		offset += 1
		i += 1
	
	while i % a % b != i % b % a:
		i += 1
	
	period = i
	hits = period - offset
	
	print ("period: {}".format(period))
	print ("offset: {}".format(offset))
	
	sol = []
	for i in range(len(l)):
		li = l[i]
		ri = r[i] + 1
		
		val = 0
		ps = li // period #starting period
		pe = ri // period #ending period
		
		si = ps * period #starting period index
		ei = pe * period #ending period index
		
		# case 1, same period
		if ps - pe = 0:
			pass
			
		# case 2, adjacent periods
		if ps - pe == 1:
			pass
		
		# case 3, seperate periods
		else:
			pass
		
		
		if li >= period:
			phase = li % period
			if phase >= hits:
				val += hits
			else:
				val += phase
		
		
		#val += ((ri - li) // period) * hits
		
		# tail of query
		phase = ri % period
		if phase - offset > 0:
			val += phase - offset
		
		sol.append(str(val))
	
	return ' '.join(sol)
		


# Main
t = read_int()
for case in range(t):
	a, b, q = read_ints()
	l = []
	r = []
	for i in range(q):
		li, ri = read_ints()
		l.append(li)
		r.append(ri)
				
	sol = solve(a, b, l, r)
	
	print (sol)
