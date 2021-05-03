"""
Red black trees. = self balancing BST

1) root is black; none children of leavese are black
2) There eare no 2 adjacent reds: self with parent or with child.
3) Every node is red or black
4) Every path from root to leaf has the same number of black nodes.

Insert, Search, Delete O(logn); h < log2(n+1). Used in k-means implementation.
AVL more balanced but more rotations 

With insert rebalance and recolor.
0 = RED; 1 = Black

"""

class Node:
	def __init__(self, val, color=0):
		self.val = val
		self.color = color
		self.left = None 
		self.right = None
		self.parent = None



class RB:
	def __init__(self, root):
		self.root = root # black

	def inorder(self, root):
		if not root:
			return 
		self.inorder(root.left)
		print(root.val)
		self.inorder(root.right)

	def _insert(self, root, node):
		"""regular bst insert"""
		if not root:
			return node
		if node.val < root.val:
			root.left = self.insert(root.left, node)
			root.left.parent = root 
		elif node.val > root.val:
			root.right = self.insert(root.right, node)
			root.right.parent = root 

		return root

	def rotate_left(self, root, node):
		tmp = node.right
		node.right = tmp.left

		if node.right:
			node.right.parent = node 

		tmp.parent = node.parent

		if not node.parent:
			root = tmp

		elif node == node.parent.left:
			node.parent.left = tmp

		else:
			node.parent.right = tmp

		tmp.left = node 
		node.parent = tmp # not sure if this is correct; need to visualize rotation with the parent.

	def rotate_right(self, root, node):
		tmp = node.left

		node.left = tmp.right

		if node.left:
			node.left.parent = node 

		tmp.parent = node.parent

		if not node.parent:
			root = tmp
		elif node.parent.left == node:
			node.parent.left = tmp
		else:
			node.parent.right = tmp 

		tmp.right = node
		node.parent = tmp # i think this is fine

	def fix_violation(self, root, node):
		# inserted node is red at first
		parent = None
		gran = None
		# 1 = black

		while node != root and node.color != 1 and node.parent.color == 0:
			parent = node.parent
			gran = node.parent.parent

			# case a: parent is left child of granparent

			if gran.left == node:
				uncle = gran.right
				# case 1; uncle is red; recolor and move node to granparent
				if uncle and uncle.col == 0:
					uncle.col = 1
					parent.col = 1
					gran.col = 0
					node = gran 

				else:
					# Case 2: node is right child of its parent: rotate
					if node == parent.right:
						self.rotate_right(root, parent)
						node = parent
						parent = node.parent

					# case 3: node is left child of the parent, rotation right necessary
					rotate_right(root, gran)
					swap(parent.col, gran.col)
					node = parent

			# Case B; paernt of pt is right child of gran
			else:
				gran = parent.left
				# recoloring case 1
				if uncle != None and uncle.col == 0: #red
					gran.col = red
					par.col = black
					uncle.col = black
					node = gran
				else:
					if node == parent.left:
						rotate_right(root, parent)
						node = parent
						parent = node.parent

					# case 3
					rotate_left(root, gran)
					swap(par.color, gran.color)
					node = parent

			root.col = black 




# deletion is even more complex

			

	def inorder(self, key):

		root = self.root
		node = Node(key, col=0) # red

		self.fix_violation(root, pt)












