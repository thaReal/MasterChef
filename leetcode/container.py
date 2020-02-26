#!/usr/bin/python3

def maxArea(height):
	n = len(height)
	mx = 0
	for i in range(int(n/2)):
		a1 = int(height[i]) * int(height[-1])
		a2 = int(height[0]) * int(height[-(i+1)])
		mx = max(mx, a1, a2)
	return mx
	
if __name__=='__main__':
	data = input()
	maxArea(data)

