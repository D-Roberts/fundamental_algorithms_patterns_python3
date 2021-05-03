


a = [4, 3, 2, 5]
heap_sort(a)
print(a)


""" Main advantage is Union of 2 heaps in O(logn) time. all other ops as in binary heap.
Maintain min heap in binomial trees. I think a list of trees in degree order
union: larger root becomes left child.
k levels; 2*k trees: go to 2 to k from 2 of 2 to k -1. Num nodes is n choose k at level k

(to be contiued at some point)
https://www.sanfoundry.com/python-program-implement-binomial-heap/
"""
class BinHeapNode:
	def __init__(self, val):
		self.val = val
		self.degree = 0
		self.children = [] 
	def add_at_end(self, t):
		self.children.append(t)
		self.degree += 1
		
		

class BinHeap:
	def __init__(self, val):
		self.h = [] # I think list of binomial trees.

	def get_min(self):
		if not self.h:
			return None

		least = self.h[0].val
		for tree in self.h:
			if tree[0] < least:
				least = tree[0]

		return least

	def combine_roots(self, h): # i think two bin heaps
		self.h.extend(h.h)
		self.h.sort(key=lambda tree: tree.degree)

	






