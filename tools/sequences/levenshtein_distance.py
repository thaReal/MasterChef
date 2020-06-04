#!/usr/bin/python3

'''
Psuedocode to compute the Levenstein Distance between two words. I'm not sure
if the resulting distance is equivalent to the 'optimal edit distance'

function LevenshteinDistance(char s[1..m], char t[1..n]):
  // for all i and j, d[i,j] will hold the Levenshtein distance between
  // the first i characters of s and the first j characters of t
  
  declare int d[0..m+1, 0..n+1] - OK
  set each element in d to zero - OK
 
  // source prefixes can be transformed into empty string by
  // dropping all characters
  
  for i from 1 to m + 1: - OK
      d[i, 0] := i - OK
 
  // target prefixes can be reached from empty source prefix
  // by inserting every character
  
  for j from 1 to n + 1: - OK
      d[0, j] := j - OK
 
 
  for j from 1 to n + 1: - OK
      for i from 1 to m + 1: - OK
          if s[i] = t[j]: - OK
            substitutionCost := 0 - OK
          else: - OK
            substitutionCost := 1 - OK

          d[i, j] := minimum(d[i-1, j] + 1,                   // deletion
                             d[i, j-1] + 1,                   // insertion
                             d[i-1, j-1] + substitutionCost)  // substitution
 
  return d[m + 1, n + 1]
'''



# Given two words word1 and word2, find the minimum number of operations 
# required to convert word1 to word2.

def minDistance(word1: str, word2: str) -> int:
	m = len(word1)
	n = len(word2)
	d = [[0 for _ in range(n+1)] for _ in range(m+1)]
	
	for i in range(1, m+1):
		d[i][0] = i
		
	for j in range(1, n+1):
		d[0][j] = j
		
	
	for j in range(1, n+1):
		for i in range(1, m+1):
			if word1[i-1] == word2[j-1]:
				cost = 0
			else:
				cost = 1
			
			d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + cost)
	
	# Debug
	#for row in d:
	#	print (row)

	return d[-1][-1]


	
if __name__=='__main__':
	word1 = "horse"
	word2 = "ros"
	sol = minDistance(word1, word2)
	print (sol)
	#Output: 3
	
	word1 = "intention"
	word2 = "execution"
	sol = minDistance(word1, word2)
	print (sol)
	#Output: 5

