#!/usr/bin/python

def solve(n, an):
	output = list()
	mina = 0
	mini = 0
	
	for i in range(n):
		if an[i] >= 0:
			j = (-an[i] - 1)
			output.append(j)
			if j < mina:
				mina = j
				mini = i
		else:
			output.append(an[i])
			if an[i] < mina:
				mina = an[i]
				mini = i	 

	if n % 2 == 1:
		output[mini] = -mina - 1
		
	# theres probably a better way to do this that saves *some* time
	out_l = [str(x) for x in output]
	outstr = " ".join(out_l)
	
	return outstr
	

# Main
n = int(raw_input())
an = [int(x) for x in raw_input().split(" ")]

output = solve(n, an)
print output
