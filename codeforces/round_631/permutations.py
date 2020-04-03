#!/usr/bin/python3

# Codeforces - Round 631
# Problem B - Dreamoon Likes Permutations


# Utilility Functions

def read_int():
	n = int(input())
	return n


def read_ints():
	ints = [int(x) for x in input().split(" ")]
	return ints

	
def check_perm(p):
	cntr = [0] * len(p)
	lmt = len(p)
	for i in p:
		if not 1 <= i <= lmt:
			return 0
		else:
			if cntr[i-1] != 0:
				return 0
			else:
				cntr[i-1] = 1
	return 1
	


# Main
t = read_int()
for case in range(t):
	n = read_int()
	a = read_ints()
	
	perms = []
	amx = max(a)
	
	p1 = (a[:amx], a[amx:])
	p2 = (a[-amx:], a[:-amx])
	
	if check_perm(p1[0]) and check_perm(p1[1]):
		perms.append((max(p1[0]), max(p1[1])))
	
	if check_perm(p2[0]) and check_perm(p2[1]):
		if (max(p2[1]), max(p2[0])) not in perms:
			perms.append((max(p2[1]), max(p2[0])))
					
	print (len(perms))
	for i in perms:
		print ("{} {}".format(i[0], i[1]))
		
		
		
