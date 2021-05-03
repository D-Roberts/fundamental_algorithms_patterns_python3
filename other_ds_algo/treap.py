"""
Treap (A Randomized Binary Search Tree):

- self balancing BST
- 2 keys: val like BST; random number (called priority) with max heap property.
- O(logn) search inserte delete with high probability.
- rotate like AVL to restore max heap at insert and delete after search like in BST.
"""

class Treap:
	def __init__(self, val):
		self.val = val
		self.rn = random.randint(1, 100)
		self.left = None
		self.right = None

	def search(self, root, key):
		if not root or root.val == key:
			return root

		if root.val < key:
			return self.search(root.left, key)

		return self.search(root.right, key)

	def insert(self, root, key):
		if not root:
			return Treap(key)

		if key <= root.key:
			root.left = self.insert(root.left, key)

			if root.left.rn < root.rn:
				root = self.right_rotate(root)

		elif key > root.key:
			root.right = self.insert(root.right, key)

			if root.right.rn < root.rn:
				root = self.left_rotate(root)

		return root

	def delete(self, root, key):
		if not root:
			return root

		if key < root.val:
			root.left = self.delete(root.left)

		elif key > root.val:
			root.right = self.delete(root.right)

		elif key == root.key and not root.left:
			temp = root.right
			root = None
			root = temp

		elif key == root.key and not root.right:
			temp = root.left
			root = None
			root = temp

		elif key == root.key and root.left.rn < root.right.rn:
			# both children alive and the one left is smaller priority
			root = self.rotate_left(root)
			root.left = self.delete(root.left)

		else: # case when node to delete has both children and right node has higher priority
			root = self.rotate_right(root)
			root.right = self.delete(root.right)

class RTree:
	"""not implemented in geeks; for geospatial coord; holds bounding boxes"""


