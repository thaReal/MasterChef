#!/usr/bin/python3

def expand(s: str, start: int, end: int) -> str:
	while start >= 0 and end <= len(s) - 1:
		if s[start] != s[end]:
			break
		start -= 1
		end += 1
	return s[start+1:end]
		

def longestPalindrome(s: str) -> str:
	lp = ""
	n = len(s)
	if n == 0:
		return ""
	elif n == 1:
		return s
	
	for i in range(n):
		cand = expand(s, i, i)
		if len(cand) > len(lp):
			lp = cand
		cand = expand(s, i, i+1)
		if len(cand) > len(lp):
			lp = cand
	return lp
				

			
if __name__ == '__main__':
	print(longestPalindrome("babad")) # bab
	print(longestPalindrome("cbbd"))  # bb
	print(longestPalindrome(""))      # ""
