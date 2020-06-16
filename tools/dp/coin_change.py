#!/usr/bin/python3

'''
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
'''

# Main Solver Function
#! -

def change(amount, coins, debug=False) -> int:
	if amount == 0:
		return 1
		
	m = len(coins)
	dp = [[0 for i in range(m)] for j in range(amount + 1)]
	
	for i in range(m):
		dp[0][i] = 1
	
	for i in range(1, amount + 1):
		
		for j in range(m):
		
			# solutions including coins[j]
			if i-coins[j] >= 0:
				x = dp[i - coins[j]][j]
			else:
				x = 0
			
			# solutions excluding coins[j]
			if j >= 1:
				y = dp[i][j-1]
			else:
				y = 0
			
			# total
			dp[i][j] = x + y
	
	if debug:
		for row in dp:
			print (row)
		print ('')
	
	return dp[-1][-1]
	
	
	
# Test Cases
# !-



amount = 5
coins = [1, 2, 5]
sol = change(amount, coins, debug=True)
print (sol)
#Output: 4
