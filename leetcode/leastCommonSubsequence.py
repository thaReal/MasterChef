#!/usr/bin/python3



def LCS_length(A, B):
	C = [[0 for x in range(len(A)+1)] for y in range(len(B)+1)]
	for i in range(1, len(A)+1):
		for j in range(1, len(B)+1):
			if A[i-1] == B[j-1]:
				C[i][j] = C[i-1][j-1] + 1
			else:
				C[i][j] = max(C[i][j-1], C[i-1][j])
	return C[-1][-1]
		
	

if __name__=='__main__':
	A = [1,1,3,5,3,3,5,5,1,1]
	B = [2,3,2,1,3,5,3,2,2,1]
	
	lcs = LCS_length(A,B)
	print ("LCS Length: {}".format(lcs))
	

