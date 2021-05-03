"""
KD trees

represents k -dim points
A none-leaf point separate space in k - 1 half spaces.
- non-leaf node: A aligned, a = D mod K (k=2 eg: either x = 0 or y = 1)
- Eg: for 2 dim
start with root: x aligned 
- next point: compare x dim to root x (go left or right
- next point insert: compare x to root and y to root's child etc

search in O(logn) time


Alternative to the k-closest points max heap variant with custom distance fct when a lot of points, k small
knn desired in many queries. (from scipy import spatial; spatial.KDTrees(points))
"""

class Node:
	def __init__(self, arr, k=2):
		self.point = arr
		self.k = k
		self.right = None
		self.left = None

	def _insert(self, root, point, depth):
		if root is None:
			return Node(point, len(point))
		cd = depth % k
		if point[cd] < root.point[cd]:
			root = _insert(root.left, point, depth+1)
		else:
			root = _insert(root.right, point, depth+1)
		return root

	def insert(self, root, point):
		"""Point is k dimensional array.
		Location depends on the depth- eg. root is x aligned and compare left right. 

		"""
		return self._insert(root, point, 0)

	def points_same(self, p1, p2):
		for i in range(self.k):
			if p1[i] != p2[i]:
				return False
		return True

	def search(self, root, point):
		return self._search(root, point, 0)

	def _search(self, root, point, depth):
		if root is None:
			return None
		if self.points_same(root.point, point):
			return root

		cd = depth % k

		if point[cd] < root.point[cd]:
			return _search(root.left, point, depth + 1)

		return _search(root.right, point, depth + 1)


# n-ary trees

class NaryNode:
    def __init__(self, val=None, children=None): # childreen can be list of nodes
        self.val = val
        self.children = children

    def preorder(self, root):
        """iterative. Visit root then children from left to right. If child has children do for them"""
        if not root:
            return []
        stack, out = [], []

        while stack:
            root = stack.pop()
            out.append(root.val)
            stack.extend(root.children[::-1])
        return out


