#!/usr/bin/python3

'''
This really needs to get updated. It kind of went to crap in the 
scramble to produce a valid solution for the leetcode problem I
developed it for.
'''

# A class that represents an individual node in a BST 
class TreeNode: 
	def __init__(self, val): 
		self.left = None
		self.right = None
		self.val = val

	# A utility function to insert a new node with the given key 
	def insert(self, val):
		if self.val:
			if val < self.val: 
				if self.left is None: 
					self.left = TreeNode(val) 
				else: 
					self.left.insert(val) 
			elif val > self.val:
				if self.right is None:
					self.right = TreeNode(val)
				else: 
					self.right.insert(val)
		else:
			self.val = val

	# A utility function to do inorder tree traversal 
	
	def inorder(self): 
		if root: 
			inorder(root.left) 
			print(root.val) 
			inorder(root.right) 

	def inorder_traversal(self, tree=[]):
		if self.left:
			self.left.inorder_traversal(tree)

		tree.append(self.val)

		if self.right:
			self.right.inorder_traversal(tree)
			
		return tree
		
		
def build_tree(root):
	n = len(root)
	for i in range(n):
		val = root[i]
		
		# conversion of None values -> Need a better way to handle this
		if val == None:
			val = 0
			
		if i == 0:
			tree = TreeNode(val)
		else:
			tree.insert(val)
	return tree
    
    
def kthSmallest(root: TreeNode, k: int) -> int:
	tree = build_tree(root)
	inorder = tree.inorder_traversal()
	for i in range(len(inorder)):
		if inorder[i] != 0:
			inorder = inorder[i:]
			break
	
	return inorder[k-1]
	
	
if __name__ == '__main__':
	# test()
	# root = [3,1,4,None,2]
	# k = 1
	
	#root = [5,3,6,2,4,None,None,1]
	#k = 3
	root = [4,2,5,1,3]
	k = 5
	
	sol = kthSmallest(root, k)
	print (sol)
	

