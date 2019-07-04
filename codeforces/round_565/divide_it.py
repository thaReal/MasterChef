

def divide_it(num, moves=0):
	if num == 1:
		return moves
		
	if num % 2 == 0:
		moves += 1
		return divide_it((num/2), moves)
	
	if num % 3 == 0:
		moves += 1
		return divide_it((2 * num / 3), moves)
	
	if num % 5 == 0:
		moves += 1
		return divide_it((4 * num / 5), moves)
	
	return -1

# Main
n = int(raw_input())
for i in range(n):
	test = int(raw_input())
	solution = str(divide_it(test))
	print solution
