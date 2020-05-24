#!/usr/bin/python3

# intersection_intervals.py: Danny Ruland
# Description: Calculate the intersection of multiple intervals

'''
Given two lists of closed intervals, each list of intervals is pairwise
disjoint and in sorted order.

Return the intersection of these two interval lists.
'''


def intervalIntersection(A, B):
	ilist = []
	i = 0
	j = 0
	while i < len(A) and j < len(B):
		ivalA = A[i]
		ivalB = B[j]
		
		if ivalB[0] > ivalA[1]:
			i += 1
			continue
		
		if ivalB[1] < ivalA[0]:
			j += 1
			continue
			
		# if neither previous case is true, then we have an intersection
		intersection = []
		
		# intersection starts at the larger of the two interval start values
		start = max(ivalA[0], ivalB[0])
		intersection.append(start)
		
		# if endpoints are the same, this is end of intersection
		# -> advance both elements
		if ivalA[1] == ivalB[1]:
			intersection.append(ivalA[1])
			i += 1
			j += 1

		# otherwise smaller endpoint is the end of the intersection
		# -> advance only the smaller elements index
		elif ivalA[1] < ivalB[1]:
			intersection.append(ivalA[1])
			i += 1
			
		else:
			intersection.append(ivalB[1])
			j += 1
	
		# add intersection to our list and continue		
		ilist.append(intersection)
	
	return ilist
	
	
	
if __name__=='__main__':
	A = [[0,2],[5,10],[13,23],[24,25]]
	B = [[1,5],[8,12],[15,24],[25,26]]
	
	sol = intervalIntersection(A, B)
	print(sol)

	# Solution: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
