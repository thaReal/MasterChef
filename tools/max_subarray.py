#!/usr/bin/python3

'''
Functions for determining max contiguous subarray for a given array.
Also additional functions for derivative problems.
'''

def max_subarray(arr):
	'''
	Find the maximum sum of a contiguous subarray of a given array.
	Solution implements Kadane's Algorithm.
	'''
	dp = [0 for i in range(len(arr))]
	dp[0] = arr[0]
	for i in range(1, len(arr)):
		dp[i] = max(dp[i-1] + arr[i], arr[i])
	#print(dp)
	return max(dp)
	

def max_subarray2(arr):
	'''
	Alternate, less elegant version implementing Kadane's Algorithm
	'''
	best_sum = 0
	current_sum = 0
	
	for x in arr:
		current_sum = max(0, current_sum + x)
		best_sum = max(best_sum, current_sum)
	
	return best_sum


def max_subarray_index(arr):
	'''
	Finds and returns the maximum sum or a contiguous subarray of a given
	array and the start and end indicies of the subarray. Solution implements
	Kadane's Algorithm and dynamic programming. Complexity is O(n).
	'''
	best_sum = 0
	best_start = best_end = 0
	current_sum = 0
	
	for current_end, x in enumerate(arr):
		if current_sum <= 0:
			current_start = current_end
			current_sum = x
		else:
			current_sum += x
		
		if current_sum > best_sum:
			best_sum = current_sum
			best_start = current_start
			best_end = current_end + 1
			
	return best_sum, best_start, best_end
	

def max_subarray_circular(arr):
	l = len(arr)
	dp = [0 for i in range(2*l)]
	dp[0] = arr[0]
	for i in range(1, l):
		dp[i] = max(dp[i-1] + arr[i], arr[i])
		
	mp = l // 2
	arr1 = arr[mp:] + arr[:mp]
	dp[l] = arr1[0]
	for i in range(1, l):
		dp[i+l] = max(dp[i+l-1] + arr1[i], arr1[i])
		
	#print(dp)
	return max(dp)
	
	
if __name__ == '__main__':
	arr1 = [5, 5, -3, 5, 5]
	arr2 = [5, -3, 5]
	arr3 = [1,-2,3,-2]
	arr4 = [-2,1,-3,7,-2,2,1,-5,4]
	
	print ("Array: {}".format(arr1))
	print ("Max subarray: {}".format(max_subarray(arr1)))
	print ("Max circular array: {}".format(max_subarray_circular(arr1)))
	
	print ("Array: {}".format(arr2))
	print ("Max subarray: {}".format(max_subarray(arr2)))
	print ("Max circular array: {}".format(max_subarray_circular(arr2)))

	
