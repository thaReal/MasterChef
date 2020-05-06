#!/usr/bin/python3

# Codeforces - Round 639
# Problem B - Card Constructions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints
	

#---

def gen_height_map():
	ht_step = 5
	hmap = [2]
	val = hmap[0]
	while val <= pow(10, 9):
		val += ht_step
		hmap.append(val)
		ht_step += 3
	
	return hmap


def get_height(hmap, n):
	i = 0
	ht = hmap[i]
	while ht <= n:
		i += 1
		ht = hmap[i]
		
	i -= 1
	rem = n - hmap[i]
	
	return rem

	
def solve(hmap, n):
	if n < 2:
		return 0
	
	cnt = 1
	rem = get_height(hmap, n)
	while rem >= 2:
		cnt += 1
		rem = get_height(hmap, rem)
		#print (rem)
		
	return cnt


# Main
t = read_int()
hmap = gen_height_map()

for case in range(t):	
	n = read_int()
	sol = solve(hmap, n)
	
	print (sol)


