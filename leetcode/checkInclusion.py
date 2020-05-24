#!/usr/bin/python3

def checkInclusion(s1: str, s2: str) -> bool:
	if len(s2) > len(s1):
		return False
        
	from collections import Counter
        
	cntr2 = Counter(s2)
	l1 = len(s1)
	l2 = len(s2)
        
	cntr1 = Counter(s1[:l2])
	if cntr1 == cntr2:
		return True
        
	for i in range(1, l1 - l2+1):
		cntr1[s1[i-1]] -= 1
		if cntr1[s1[i-1]] == 0:
			cntr1.pop(s1[i-1])
		cntr1[s1[i + l2 - 1]] += 1
		
		print (cntr1) #debug
		
		if cntr1 == cntr2:
			return True
		
	return False
		
if __name__ == '__main__':
	s1 = "dcda"
	s2 = "adc"
	
	print (checkInclusion(s1, s2))
