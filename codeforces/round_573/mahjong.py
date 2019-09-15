#!/usr/bin/python

# Main
 
data = [x for x in raw_input().split(" ")]
sol = None
 
if len(set(data)) == 1:
	sol = 0
 
elif data[0][1] == data[1][1] and data[0][1] == data[2][1]:
	nums = [int(data[0][0]), int(data[1][0]), int(data[2][0])]
	nums.sort()
	if nums[0] == nums[1] - 1:
		if nums[1] == nums[2] - 1:
			sol = 0
		else:
			sol = 1
	else:
		if nums[1] == nums[2] - 1:
			sol = 1
 
elif len(set(data)) == 2:
	if sol != 0:
		sol = 1
		
		
# I think this entire block is redundants since I handled it in the 
# check above... That said, I don't think it'll hurt - worst case if
# I'm right, it'll just fire down this branch in the case of a 2
 
if sol == None:
	if data[0][1] == data[1][1]:
		if abs(int(data[0][0]) - int(data[1][0])) <= 2:
			# they're off by one and we only need one more piece
			sol = 1
	
	if data[0][1] == data[2][1]:
		if abs(int(data[0][0]) - int(data[2][0])) <= 2:
			# they're off by one and we only need one more piece
			sol = 1
	
	if data[1][1] == data[2][1]:
		if abs(int(data[1][0]) - int(data[2][0])) <= 2:
			# they're off by one and we only need one more piece
			sol = 1
 
if sol == None:
	sol = 2
 
print sol
