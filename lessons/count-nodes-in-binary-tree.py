"""
Given the root to a binary tree, count the total number of nodes there are.

"""

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def count(node):
	return count(node.left) + count(node.right) + 1 if node else 0

if __name__ == "__main__":
	tree = Node(4, Node(2, Node(1), Node(3)), Node(5))
	"""
	    4
	   / \
	  2   5
	 / \  
	1   3
	  
	"""
	print(count(tree))
