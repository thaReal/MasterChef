#!/usr/bin/python3

'''
This really needs to get updated. It kind of went to crap in the 
scramble to produce a valid solution for the leetcode problem I
developed it for.

*Update: Getting better, need to still scrub this and add the leetcode
built-ins.
'''


# A class that represents an individual node in a BST 
class TreeNode: 
	def __init__(self, val): 
		self.left = None
		self.right = None
		self.val = val

	# A utility function to insert a new node with the given key
	# DEPRECEATED: TO BE DELTED
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


	def inorder_traversal(self, tree=[]):
		'''Returns all elements starting from the leftmost child
		resulting in an in-order arrangement of values'''
		if self.left:
			self.left.inorder_traversal(tree)
		tree.append(self.val)
		if self.right:
			self.right.inorder_traversal(tree)
			
		return tree
		
	def preorder_traversal(self, tree=[]):
		pass
		
		
# -----
		
		
def build_tree(root):
	'''This was specific to the kthSmallest problem. Not sure exactly what
	I'm trying to accomplish here'''
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
	
def test_kthSmallest():
	# root = [3,1,4,None,2]
	# k = 1
	
	#root = [5,3,6,2,4,None,None,1]
	#k = 3
	
	root = [4,2,5,1,3]
	k = 5
	
	sol = kthSmallest(root, k)
	print (sol)


# -----


def bstFromPreorder(preorder):
	for i in range(len(preorder)):
		if i == 0:
			root = TreeNode(preorder[i])
		else:
			root.insert(preorder[i])
	return root


# -----


def sortedArrayToBST(nums: List[int]) -> TreeNode:
	'''
	Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

	For this problem, a height-balanced binary tree is defined as a binary tree in which the 
	depth of the two subtrees of every node never differ by more than 1.
	'''

	if len(nums) == 0:
		return None

	if len(nums) == 1:
		node = TreeNode(nums[0])
		return node

	idx = len(nums) // 2
	node = TreeNode(nums[idx])
	ltree = nums[:idx]
	rtree = nums[idx+1:]

	if len(ltree) > 0:
		node.left = sortedArrayToBST(ltree)

	if len(rtree) > 0:
		node.right = sortedArrayToBST(rtree)

	return node


	
if __name__ == '__main__':
	#test_kthSmallest()
	preorder = [8,5,1,7,10,12]
	root = bstFromPreorder(preorder)
	print (root.inorder_traversal())
	
	

