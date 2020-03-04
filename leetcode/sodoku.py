#!/usr/bin/python3

candidates = [1,2,3,4,5,6,7,8,9]

class Sodoku(object):
	def __init__(self, puzzle):
		self.rows = puzzle
		print (puzzle)
		
		self.columns = []
		for i in range(9):
			column = []
			for j in range(9):
				column.append(puzzle[j][i])
			self.columns.append(column)
		
		self.boxes = []
		for i in range(9):
			box = []
			for j in range(3):
				row = []
				for k in range(3):
					y = int(i/3) + j
					x = (i % 3) * 3 + k
					row.append(puzzle[y][x])
				box.append(row)
			self.boxes.append(box)
	
	
	def count_blanks(self):
		blanks = 0
		for row in self.rows:
			blanks += row.count(0)
		return blanks
		
		
	def breadth_search(self):
		for n in candidates:
			for box in boxes:
				cand_rows = []
			
			
	def solve(self):
		while count_blanks(self) != 0:
			break
	
	
	# DEBUG
	def print_boxes(self):
		for box in self.boxes:
			print (box)
			
	def print_columns(self):
		for column in self.columns:
			print (column)


	
if __name__=='__main__':
	data = input().split(" ")
	puzzle = []
	for i in data:
		row = []
		for j in i:
			row.append(int(j))
		puzzle.append(row)	
		
	
	if len(puzzle) == 9:
		sodoku = Sodoku(puzzle)
		print("\nBoxes:")
		sodoku.print_boxes()
		print("\nColumns:")
		sodoku.print_columns()
	else:
		print ("Input Error")


