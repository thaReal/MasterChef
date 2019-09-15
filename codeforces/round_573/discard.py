#!/usr/bin/python
from collections import deque

# Main
data = [int(x) for x in raw_input().split(" ")]
n = data[0]
m = data[1]
k = data[2]

opr = 0 #operation counter
offset = 0 #index offset (as a result of discarded items)
pm = deque(int(x) for x in raw_input().split(" "))

# initialize page and bounds
page = 1
ubound = page * k

ind = pm.popleft()
while True:	
	inc_offset = 1

	#jump ahead if a page doesn't require any operations
	if ubound < ind:
		page = (ind / k) + 1
		page -= 1 if (ind % k) == 0 else 0
		
		#update our bounds for the current page
		ubound = page * k
			
	#if there are no more indicies in our deque perform the 
	#operation and then break
	if len(pm) == 0:
		opr += 1
		break
		
	#now we're on the page where our next operation takes place, iteratively
	#check if the next index falls on the same page (lower than ubound) 
	while True:
		ind = pm.popleft()
		ind -= offset
		
		# if the index is below the upper bound increment inc_offset
		# and continue
		if ubound >= ind:
			inc_offset += 1
		
		# otherwise update the offset, perform the operation and break
		else:
			offset += inc_offset
			ind -= inc_offset
			opr += 1
			break
			
		# if we haven't exited the loop by now, we need to make sure that
		# we still have an item left in our deque before continuing
		if len(pm) == 0:
			
			# if not break, and perform the operation and exit naturally
			# through the next loop iteration
			break
			
print opr
