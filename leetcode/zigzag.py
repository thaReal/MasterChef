#!/usr/bin/python3

def convert(s: str, numRows: int) -> str:
	if numRows == 1:
		return s
	
	n = len(s)
	l1 = [x for x in range(numRows)] + [x for x in range(numRows-2,0,-1)]
	m = int(len(s) / len(l1)) + 1
	seq = (l1 * m)[0:n]
	
	rows = list()
	for i in range(numRows):
		rows.append([])
	
	for i in range(n):
		rows[seq[i]] += s[i]
	
	sol = ""
	for r in rows:
		sol += ''.join(r)		
	
	return sol
	
	
	
if __name__=='__main__':
	# Test Case 1
	s = "PAYPALISHIRING"
	numRows = 3
	print (convert(s, numRows)) # -> "PAHNAPLSIIGYIR"
