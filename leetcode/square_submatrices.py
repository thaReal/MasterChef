#!/usr/bin/python3
#-*- coding: utf-8 -*-

'''
Given a m * n matrix of ones and zeros, return how
many square submatrices have all ones.
'''

def countSquares(matrix):
	'''Returns the largest square region of 1's in
	the input matrix. Works; but runs in I believe 
	O(1^n) time, so does not pass tests'''
	h = len(matrix)
	w = len(matrix[0])
	
	sz = min(h, w) #maximum size of a potentially full square
	cnt = 0
	while sz > 0:
		for i in range(h-sz+1):
			submat = matrix[i:i+sz]
			for j in range(w-sz+1):
				valid = True
				for row in submat:
					if 0 in row[j:j+sz]:
						valid = False
						break
				if valid:
					cnt += 1
		sz -= 1
	return cnt
	

def additiveTable(matrix):
	h = len(matrix)
	w = len(matrix[0])
	
	table = []
	for i in range(h):
		row = [None] * w
		table.append(row)
		
	for i in range(h):
		for j in range(w):
			val = matrix[i][j]
			if i == 0 and j == 0:
				table[i][j] = val
			
			elif i == 0:
				table[i][j] = table[i][j-1] + val
			
			elif j == 0:
				table[i][j] = table[i-1][j] + val
			
			else:
				table[i][j] = val + table[i][j-1] + table[i-1][j] - table[i-1][j-1]

	
	return table
			
	
def countSquares2(matrix):
	table = additiveTable(matrix)
	
	# first get height and width of rectangular matrix
	h = len(table)
	w = len(table[0])
	
	sz = min(h, w)
	cntr = 0
	while sz > 1:
		# our starting index is the outer corner of the submatrix
		# and then our calculations subtract two submatrix values
		# in order to check if array is valid
		
		for i in range(sz-1, h):
			for j in range(sz-1, w):
				if j-sz >= 0:
					if i-sz >= 0:
						# subtract prior rows
						c1 = table[i-sz][j] - table[i-sz][j-sz]
						# subtract prior columns
						c2 = table[i][j-sz]
					else:
						# just subtract prior columns
						c1 = 0
						c2 = table[i][j-sz]
					
				else:
					if i-sz >= 0:
						# just subtract prior rows
						c1 = table[i-sz][j]
						c2 = 0
					else:
						c1 = c2 = 0
				
				# finally check if the value at our current index is 
				# equal to sz**2 - c1 - c2
				val = table[i][j] - c1 - c2
				if val == sz**2:
					cntr += 1
	
		sz -= 1
	
	# Last, use list.count() rather than additive table method to 
	# speed up case where sz=1 			
	
	for row in matrix:
		cntr += row.count(1)
	
	return cntr


'''
Notes:

sz = 3
[ 0 1 2  3 ]  [ 0 1 ]
[ 1 3 5  7 ]
[ 1 4 7 10 ]
	
sz = 2
[ 0 1 2  3 ]  [ 0 1 1 ]
[ 1 3 5  7 ]
	
sz = 2,
[ 1 3 5  7 ]  [ 0 1 1 ]
[ 1 4 7 10 ]
	
'''


	
if __name__=='__main__':
	matrix1 = [ 
  		[0,1,1,1],
  		[1,1,1,1],
  		[0,1,1,1]
	]
	
	matrix2 = [
  		[1,0,1],
  		[1,1,0],
  		[1,1,0]
	]
	
	matrix3 = [
		[0, 0, 0],
		[0, 0, 0]
	]
	
	
	cnt = countSquares2(matrix1)
	print (cnt)

	cnt = countSquares2(matrix2)
	print (cnt)
	
	
