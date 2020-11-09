#!/usr/bin/python3

'''
binary_tree.py - Author: Daniel Ruland
Description: Basic Binary Tree Reference Implementation with common functions
'''

#-----
class TreeNode: 
	'''A class that represents an individual node in a BST'''
	def __init__(self, val): 
		self.left = None
		self.right = None
		self.val = val


#-------------------#
# Utility Functions #
#-------------------#

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"
    
    
def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root
    
    
def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)


#---------------------#
# Traversal Functions #
#---------------------#

# Pay attention to the implementation of these calls. If there are multiple calls in a loop.
# the environment may not pass an empty tree to successive calls (as is expected). To deal 
# with these situations, create an empty tree (in the calling loop) prior to each function call

def inorder_traversal(node, tree=[]):
	'''Returns all elements starting from the leftmost child
	resulting in an in-order arrangement of values'''
	if node.left:
		inorder_traversal(node.left, tree)
	
	tree.append(node.val)
	
	if node.right:
		inorder_traversal(node.right, tree)
		
	return tree
		
		
def preorder_traversal(node, tree=[]):
	tree.append(node.val)
	
	if node.left:
		preorder_traversal(node.left, tree)
	
	if node.right:
		preorder_traversal(node.right, tree)
	
	return tree
		
		
def postorder_traversal(node, tree=[]):
	if node.left:
		postorder_traversal(node.left, tree)
	
	if node.right:
		postorder_traversal(node.right, tree)
		
	tree.append(node.val)
	
	return tree


	
if __name__ == '__main__':
	# Misc Test Driver
	rootstr = "[4,2,9,3,5,null,7]"
	root = stringToTreeNode(rootstr)
	print ("Binary Tree:\n")
	prettyPrintTree(root)
	
	print("\nInorder Traversal:")
	print(inorder_traversal(root))

	print("\nPostorder Traversal:")
	print(postorder_traversal(root))
	
	print("\nPreorder Traversal:")
	print(preorder_traversal(root))
