#!/usr/bin/python3

# Leetcode May Challenge: Flood Fill
# Author: Danny Ruland

def floodFill(image, sr, sc, newColor):
	from collections import deque
	d = deque()
	d.append([sr, sc])
        
	visited = set()
	newImage = image
	oldColor = image[sr][sc]
	
	rmax = len(image)
	cmax = len(image[0])
        
	while len(d) > 0:
		print (d) #Debug
		
		r, c = d.popleft()
		visited.add((r,c))
		newImage[r][c] = newColor
		adjacent = [[r, c+1], [r, c-1], [r+1, c], [r-1, c]]
                            
		for cell in adjacent:
			r, c = cell
			if r < 0 or r >= rmax:
				continue
				
			if c < 0 or c >= cmax:
				continue
            
			if (r,c) in visited:
				continue
				
			val = image[r][c]            
			if val == oldColor:
				d.append([r,c])
                    
	return newImage
	
	
if __name__=='__main__':
	image = [[1,1,1],[1,1,0],[1,0,1]]
	sr = 1
	sc = 1
	newColor = 2
	
	print (floodFill(image, sr, sc, newColor))
