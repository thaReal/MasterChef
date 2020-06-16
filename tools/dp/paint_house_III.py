#!/usr/bin/python3


def build_cost_matrix(houses, cost, m , n):
	cost_matrix = [[0 for i in range(m)] for j in range(n+1)]
	for j in range(n):
		for i in range(m):
			if houses[i] != j+1:
				try:
					cost_matrix[j+1][i] = cost[i][j]
				except:
					print ("{} {}".format(j, i))
					return None
	return cost_matrix	



if __name__=='__main__':
	houses = [0,0,0,0,0]
	cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
	m = 5
	n = 2
	target = 3
	
	sol = build_cost_matrix(houses, cost, m, n)
	for row in sol:
		print (row)
