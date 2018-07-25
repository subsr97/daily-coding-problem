"""
Given the root to a binary tree, return the deepest node.

"""

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return "<" + str(self.val) + ">"

def deepest(node):
	if node and not node.left and not node.right:
		return (node, 1) # Leaf and its depth

	if not node.left: # Then the deepest node is on the right subtree
		return increment_depth(deepest(node.right))
	elif not node.right: # Then the deepest node is on the left subtree
		return increment_depth(deepest(node.left))

	return increment_depth(
			max(deepest(node.left), deepest(node.right),
					key=lambda x: x[1]))

def increment_depth(node_depth_tuple):
	node, depth = node_depth_tuple
	return (node, depth + 1)

if __name__ == "__main__":
	tree = Node(4, Node(2, Node(1, Node(0)), Node(3)), Node(5))
	"""
		    4
		   / \
		  2   5
		 / \  
		1   3
	       /
	      0
	"""
	node_depth_tuple = deepest(tree)
	print(node_depth_tuple[0], " of depth ", node_depth_tuple[1])
