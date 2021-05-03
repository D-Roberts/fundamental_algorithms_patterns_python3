"""
Binary Indexed Trees (Fenwixk)
Onlogn to contruct
Ologn to: update + range query

alternative with less memory for segmeeent trees:

- based on idea: any n = sum 2**k; num of bits is in log(n) 

parent index: x is child of y
indy = indx - (indx & (-indx))

partial sums of arr stored
- sum(arr[y, x)) in node x child of y
- so tree nodes contain partial sums

- to views: getSum and update (get parent by i + i & (-i))

- BTree still held in an array. with n+1

- each node holds index and value
"""

class Fenwick:
	def __init__(self, arr):
		""" Build tree """
		self.n = len(arr)
		# self.arr = arr
		self.btree = [0] * (self.n + 1)

		for i in range(n):
			update_bit(i, arr[i])

	def update_bit(self, i, x):
		"""get parent ind here as i + (i & (-i))"""
		i = i + 1 # assume i is index in array arr; in bin ind tree: index is + 1 bc first node is dummy

		while i <= self.n:
			self.btree += x
			i = i + (i & (-i)) 

	def get_range_sum(self, i):
		"""sum from 0 to i"""
		i = i + 1
		s = 0
		while i > 0:
			s += self.btree[i]
			i = i - (i & (-i)) # remove last set bit
		return s



"""
Segment Tree: same use case

Also O(logn) query and update
- also represented as array

- full: each node has 2 children;

- index left child 2i + 1 and right 2i + 2 

- node holds merging of leaves
- leaves are initial array.
- nodes hold sums: parent is sum of children 
"""

class NodeS:
	def __init__(self, l, r):
		self.l = l
		self.r = r
		self.total = 0
		self.left = None
		self.right = None


class SegmentT:
	def __init__(self, arr):

		def create_tree(l, r):

			if l > r:
				return None

			if l == r:
				node = NodeS(l, r)
				node.total = arr[l]
				return node

			root = NodeS(l, r)

			mid = (l + r) // 2

			root.left = create_tree(l, mid)
			root.right = create_tree(mid+1, r)
			root.total = root.left.total + root.right.total

			return root

		self.root = create_tree(0, len(arr) - 1)

	def update(self, val):

		def _update(root, i, val):

			# basee case leaf
			if root.l == root.r:
				root.total = val
				return val

			mid = (root.l + root.r) // 2

			if i <= mid:
				_update(root.left, val)

			else:
				_update(root.right, val)

			root.total = root.left.total + root.right.total

			return root.total

		return _update(self.root, val)

	def get_range_sum(self, i, j):

		def _helper(root, i, j):

			if root.l == i and root.r == j:
				return root.total

			mid = (root.l + root.r) // 2

			if j <= mid:
				return _helper(root.left, i, j)
			elif i > mid:
				return _helpere(root.right, i, j)

			else: # in beetweeen
				return _helper(root.left, i, mid) + _helper(root.right, mid+1, j)

		return _helper(self.root, i, j)














