#!/usr/bin/python3
import sys
from itertools import combinations

candidates = [1,2,3,4,5,6,7,8,9]

#---------#
# Classes #
#---------#

class Cell(object):
	def __init__(self, x, y, val):
		self.row = x
		self.col = y
		self.val = val
		self.box = None
		
		if self.val == 0:
			self.possibilities = set(candidates)
		else:
			self.possibilities = set()
			self.possibilities.add(self.val)
			
		self.choices = set()
		
	def __repr__(self):
		return str(self.val)
	
	
class Sodoku(object):
	def __init__(self, puzzle):
		self.rows = puzzle
		self.columns = []
		for i in range(9):
			column = []
			for j in range(9):
				column.append(self.rows[j][i])
			self.columns.append(column)
		
		self.boxes = []
		for i in range(9):
			box = []
			for j in range(3):
				for k in range(3):
					x = int(i / 3) * 3 + j
					y = (i % 3) * 3 + k
					self.rows[x][y].box = i
					box.append(self.rows[x][y])
			self.boxes.append(box)
	
	
	def count_blanks(self):
		blanks = 0
		for row in self.rows:
			for i in row:
				if i.val == 0:
					blanks += 1
					
		return blanks
		
		
	def breadth_search(self):
		for i in range(9):
			box = self.boxes[i]
			for j in box:
				if j.val == 0:
					sr = set([k.val for k in self.rows[j.row]])
					j.possibilities.difference_update(sr)
					
					sc = set([k.val for k in self.columns[j.col]])
					j.possibilities.difference_update(sc)
					
					sb = set([k.val for k in self.boxes[j.box]])
					j.possibilities.difference_update(sb)
					
					if len(j.possibilities) == 1:
						j.val = list(j.possibilities)[0]
						print ('[+] Found Cell {},{}: {}'.format(j.row, j.col, j.val))
						
						
	def depth_search(self):
		self.depth_search_iter(self.rows)
		self.depth_search_iter(self.columns)
		self.depth_search_iter(self.boxes)
					
					
	def depth_search_iter(self, obj):
		for i in range(9):
			choices = set(candidates)
			empty_cells = []
		
			for cell in obj[i]:
				if cell.val == 0:
					empty_cells.append(cell)
				else:
					choices.discard(cell.val)
		
			for c in choices:
				options = []
				for cell in empty_cells:
					if c in cell.possibilities:
						options.append(cell)
				
				if len(options) == 1:
					cell = options[0]
					cell.val = c
					cell.possibilities = set()
					cell.possibilities.add(c)
					
					print ('[+] Found Cell {},{}: {}'.format(cell.row, cell.col, cell.val))
					
					
	def possibility_reduction(self):
		pass
		
	
	def poss_reduction_iter(self, obj):
		cntr = 0
		for i in range(9):
			pos_set = set()
			empty_cells = []
			for c in obj[i]:
				if c.val == 0:
					empty_cells.append(c)
					pos_set = pos_set.union(c.possibilities)
			
			# change this to a while loop and only increment if counter doesn't
			# increase after we've tried a reduction of size N
			
			for i in range(2, len(empty_cells)-1):
				combos = combinations(pos_set, 2)
				for j in combos:
					for k in j:
						
					
		# Debug					
		print ("> Discarded {} cells.".format(cntr))
				
					
	
	def quick_search(self):
		for row in self.rows:
			for cell in row:
				if len(cell.possibilities) == 1 and cell.val == 0:
					cell.val = list(cell.possibilities)[0]
					print ('[+] Found Cell {},{}: {}'.format(cell.row, cell.col, cell.val))			
	
	#-------------------------#
	# End of search functions #
	#-------------------------#
			
	def solve(self):
		blanks = self.count_blanks()
		itr = 1
		level = 0
		
		print ("\nIteration: {}".format(itr))
		while self.count_blanks() != 0:
			# 'search level' logic
			self.search(level)
			new_blanks = self.count_blanks()
			
			if  new_blanks < blanks:
				blanks = new_blanks
				itr += 1
				level = 0
				print ("\nIteration: {}".format(itr))			
			else:
				level += 1
				if level > 2:
					break
			
			
		# End of solver once main loop has finished 
		if self.count_blanks() == 0:
			print ("\n[+] Solved!")
		else:
			print ("\n[-] Solution not found.")
			
	
	def search(self, level):
		switcher = {
				0: self.quick_search,
				1: self.breadth_search,
				2: self.depth_search
			}
			
		func = switcher.get(level, None)
		
		return func()
	
	
	def print_game(self):
		output = []
		print ("")
		sep = "-" * 13
		
		for i in range(9):
			if i % 3 == 0:
				output.append(sep)
			
			outstr = ""
			for j in range(9):
				if j % 3 == 0:
					outstr += "|"
				outstr += str(self.rows[i][j].val)
			
			outstr += "|"
			output.append(outstr)
		output.append(sep)
			
		for s in output:
			print(s)
			


#-----------#
# Functions #
#-----------#

def make_puzzle(data):
	puzzle = []
	for x in range(len(data)):
		row = []
		for y in range(len(data[x])):
			cell = Cell(x, y, data[x][y])
			row.append(cell)
		puzzle.append(row)
	
	return puzzle
	
	
def check_puzzle(data):
	valid = True
	for line in data:
		if len(line) != 9:
			valid = False
			break
			
	return valid
		

# Main Driver
def main():
	data = input().split(" ")
	valid = check_puzzle(data)
	
	if valid == False:
		print ("[-] Input Error, check puzzle data")
		sys.exit(1)
	
	puzzle_data = []
	for i in data:
		row = [int(x) for x in i]
		puzzle_data.append(row)
	
	puzzle = make_puzzle(puzzle_data)
	game = Sodoku(puzzle)
	
	blanks = game.count_blanks()
	
	print ("Solver started; {} blank cells to find.".format(blanks))
	game.print_game()
	print ("")
	game.solve()
	game.print_game()
	print ("")
	
	game.poss_reduction_iter(game.boxes)
	
	for cell in game.boxes[3]:
		print (cell.possibilities)
	
	
	
		
if __name__=='__main__':
	main()
	
	

