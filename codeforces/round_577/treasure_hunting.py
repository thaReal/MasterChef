#!/usr/bin/python
from collections import deque

# Main
l1 = [int(x) for x in raw_input().split(" ")]
n = l1[0]
m = l1[1]
k = l1[2]
q = l1[3]

treasures = []
for i in range(k):
	t = [int(x) for x in raw_input().split(" ")]
	treasures.append(t[0], t[1])

b = [int(x) for x in raw_input().split(" ")]
b.sort()

loc = [1, 1]
moves = 0
treasures.sort()
d = deque(treasures)

while len(treasures) > 0:
	# first we need to bin the treasures by row, I think I can do this as I 
	# go so I'm not adding more overhead on top of the sort earlier
	treasure_row = []
	treasure = treasures.popleft()
	treasure_row.append(treasure)
	
	while treasures[0][0] == treasure[0]:
		t2 = treasures.popleft()
		treasure_row.append(t2)
		
	# okay now we at least can deal with whatever row we're in optimally, and
	# then see what's the best route to take to get to an optimal starting
	# point for the next row once we're done with this one -- actually i don't
	# think this actually matters, the quickest route to the next row should 
	# always be the optimal choice
		
	# are we in the same row
	if loc[0] == treasure[0]:
	
	# ok, here's where the previous version is an oversimplification. We do 
	# need to first check if we're on treasure, but after that we need to 
	# find an optimal route to transverse the row and the find a 'safe exit
	# column' to advance onwards.
	
		# yes, are we on the treasure?
		if loc[1] == treasure[1]:
			# yes, got it
			continue
		else:
			# no, lets move horizontally and get it
			m = abs(loc[1] - treasure[1])
			moves += m
	else:
		# not in the same row, need to move vertically
		
		# are we in a 'safe' row?
		if loc[1] in b:
			# yes, lets move up
			m = treasure[1] - loc[1]
			moves += m
		else:
			# no, here's the hard part
			
					
