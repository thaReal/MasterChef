#!/usr/bin/python3

# Codeforces - Round 620
# Problem C - Air Conditioner


# Main
q = int(input())
for case in range(q):
	data = [int(x) for x in input().split(" ")]
	n = data[0]
	m = data[1]
	
	times = []
	temps = []
	for i in range(n):
		line = [int(x) for x in input().split(" ")]
		times.append(line[0])
		tr = (line[1], line[2])
		temps.append(tr)
		
	t_slack = 0
	t = 0
	sol = 'YES'
	for cust in range(len(times)):
		# if current temp is lower than target range
		if m < temps[cust][0]:
			d = temps[cust][0] - m
			
			# first check if it's possible to satisfy customer
			if (times[cust] - t) < d:
				
				# it's not, see if we can use slack temp to make up the diff
				if (times[cust] - t) < (d + t_slack):
					t_slack -= times[cust] - t - d
					
				# otherwise 
				else:
					sol = 'NO'
					break
			
			else:
				# if so, caluclate any slack temp for next customer
				t_slack += min(times[cust] - d, temps[cust][1] - temps[cust][0])

			# set our new current temp and time
			m = temps[cust][0] 
			t = times[cust]
			print ("temp: {}, time {}".format(m,t))
			print ("slack temp: {}".format(t_slack))
				
		# if current temp is above target range
		elif m > temps[cust][1]:
			d = m - temps[cust][1]
			
			# check if it's possible to satisfy customer
			if (times[cust] - t) > d:
				
				# it's not, see if we can use slack temp to make up the diff
				if (times[cust] - t) < (d - t_slack):
					t_slack -= d - times[cust] - t 
		
				# otherwise
				else:
					sol = 'NO'
					break
					
			else:
				# if so, calculate any slack temp for next customer
				t_slack -= max(-(times[cust] - d), temps[cust][0] - temps[cust][1])
			
			# set our new current temp and time
			m = temps[cust][1]
			t = times[cust]
			print ("temp: {}, time {}".format(m,t))
			print ("slack temp: {}".format(t_slack))
			
	print (sol)
