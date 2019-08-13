#!/usr/bin/python


# Main
n = int(raw_input())

hotel = []
for i in range(10):
	hotel.append(0)

eventstr = raw_input()
events = [x for x in eventstr]
for e in events:
	if e == "L":
		for i in range(len(hotel)):
			if hotel[i] == 0:
				hotel[i] = 1
				break
	
	elif e == "R":
		for i in range(len(hotel)-1, 0, -1):
			if hotel[i] == 0:
				hotel[i] = 1
				break
	
	else:
		room = int(e)
		hotel[room] = 0

sol = ""
for i in hotel:
	sol += str(i)
print sol
