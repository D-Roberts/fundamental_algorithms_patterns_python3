"""
Quad trees

make from grid matrix with 0 and 1
https://leetcode.com/problems/construct-quad-tree/submissions/
O(nsq) to make
should have O(logn) to search

bottom up construction from grid here
"""

class QuadNode:
	def __init__(self, val, isLeaf, tl, tr, bl, br):
		self.val = val
		self.isLeaf = isLeaf
		self.topLeft = tl
		self.topRight = tr
		self.bottomLeft = bl
		self.bottomRight = br

	def make_quad(self, grid):
		leaves = [QuadNode(0, True, None, None, None, None), 
					QuadNode(0, True, None, None, None, None)]
		def _make_quad(i, j, qsize):
			if qsize == 1:
				return leaves[grid[i][j]]

			quads = [_make_quad(i, j, qsize),
					_make_quad(i, j+qsize, qsize),
					_make_quad(i+qsize, j, qsize),
					_make_quad(i+qsize, j+qsize, qsize)]

			top_left_val = quads[0].val

			if all(q.val == top_left_val for q in quads):
				return quads[0]
			else:
				return QuadNode(1, False, *quads)


		return _make_quad(0, 0, len(grid))


	
