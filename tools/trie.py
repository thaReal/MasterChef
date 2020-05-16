#!/usr/bin/python3

'''
Basic Python 3 Trie Graph Implementation
'''

class Node:
	def __init__(self, char: str):
		'''
		Initialize Node data structure.
		'''
		self.char = char
		self.endOfWord = False
		self.children = dict()
		

class Trie:
	def __init__(self):
		'''
		Initialize trie data structure.
		'''
		self.root = Node('*')
		
	
	def insert(self, word: str) -> None:
		'''
		Inserts a word into the trie.
		'''
		node = self.root
		for i in range(len(word)):
			char = word[i]
			if char not in node.children.keys():
				node.children[char] = Node(char)
			
			node = node.children[char]
			
			if i == len(word) - 1:
				node.endOfWord = True
	
	
	def search(self, word: str) -> bool:
		'''
		Returns if the word is in the trie.
		'''
		node = self.root
		for char in word:
			if char not in node.children.keys():
				return False
				
			node = node.children[char]
		
		return True if node.endOfWord else False
			
	
	def startsWith(self, prefix: str) -> bool:
		'''
		Returns if there is any word in the trie that starts with the
		given prefix.
		'''
		node = self.root
		for char in prefix:
			if char not in node.children.keys():
				return False
				
			node = node.children[char]
		
		return True
	
		
if __name__=='__main__':
	trie = Trie()
	trie.insert("danny")
	r1 = trie.search("danny")
	r2 = trie.search("")
	r3 = trie.startsWith("dan")
	print ("r1: {}\nr2: {}\nr3: {}".format(r1,r2, r3))
