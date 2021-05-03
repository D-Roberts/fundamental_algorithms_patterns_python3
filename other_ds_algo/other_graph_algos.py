"""
Kosaraju to get strongly connected components in graph:

SCC have a path trhough each node in the SCC. directed graph.

AlgO;
Need to tackle that : start node counts; 

1. Set up graph considering directions of edges.
2. Start any v. dfs and add v to a stack: deepest node first.
3. Reverse initial graph.
4. do another dfs. Pop each node from stack (if list this is the last node) and traverse with dfs and add
to component. New component with each unvisited node popped.

O(V+E)
"""

class Kosaraju:
	def __init__(self, N):
		self.g = collections.defaultdict(list)
		self.n = N
		
	def add_edge(self, u):
		pass

	def dfs1(self, u):
		visited.add(u)
		for v in g[u]:
			if not v in visited:
				self.dfs1(v)
		stack.append(u)
		
	def dfs2(self, u, comp):
		visited.add(u)
		for v in g[u]:
			if not v in visited:
				self.dfs2(v)
		comp.add(u)

	def kosaraju(self):
		scc = []

		rg = collections.defaultdict(list)

		for u in g:
			for v in g[u]:
				rg[v].append(u)

		stack, visited = [], set()

		for u in g:
			if not u in visited:
				self.dfs1(u)

		visited = set()

		for u in stack[::-1]:
			if not u in visited:
				comp = []
				dfs2(u, comp)
				scc.append(comp)
		return scc

