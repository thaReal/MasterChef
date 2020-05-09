#!/usr/bin/python3

from binarytree import Node 

root = Node(3) 
root.left = Node(6) 
root.right = Node(8) 

# Getting binary tree 
print('Binary tree :', root) 

# Getting list of nodes 
print('List of nodes :', list(root)) 

# Getting inorder of nodes 
print('Inorder of nodes :', root.inorder) 

# Checking tree properties 
print('Size of tree :', root.size) 
print('Height of tree :', root.height) 

# Get all properties at once 
print('Properties of tree : \n', root.properties) 


# Python program to introduce Binary Tree 

# A class that represents an individual node in a 
# Binary Tree 
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 


# create root 
root = Node(1) 
''' following is the tree after above statement 
		1 
	/ \ 
	None None'''

root.left	 = Node(2); 
root.right	 = Node(3); 
	
''' 2 and 3 become left and right children of 1 
	   1 
	  / \ 
	 2	 3 
	/ \ / \ 
None None None None'''


root.left.left = Node(4); 
'''4 becomes left child of 2 
		1 
	/	 \ 
	2		 3 
	/ \	 / \ 
4 None None None 
/ \ 
None None'''



#---
# From leetcode
#---

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
