#!/usr/bin/python


# Main
l1 = [int(x) for x in raw_input().split(" ")]
n = l1[0]
k = l1[1]

a = [int(x) for x in raw_input().split(" ")]
a.sort()

M = 1
ind = n/2
val = a[ind]

while k > 0:
	if ind == n-1:
		val += k / M
		break
	
	elif a[ind+1] == val:
		M += 1
		ind += 1
		
	else:
		delta = a[ind+1] - val
		if (delta * M) > k:
			val += k / M
			break
		
		else:
			val = a[ind+1]
			k -= M * delta
			ind += 1
			M += 1

print val		
