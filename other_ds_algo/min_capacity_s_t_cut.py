"""
Problem: 
- find s-t cut of minimum capacity; return the edges

- capacity is sum of edge weights

- has a source s and a sink t; 
- get set of vertices of max flow via ford fulkerson; 
- get residual graph

- edges: from reachable vertices (from s) to non-reachable in residual graph.

- code with adjacency matrix and Fold-Fulkerson

O(v**3)
"""


class Graph:
	def __init__(self, graph, s, t):
		self.m = len(graph)
		self.n = len(graph[0])
		self.graph = graph 
		self.res_graph = [graph[i][:] for i in range(self.m)] # weights in the graph

	 # Ford-Fulkerson SLOW DOWN. DONT MAKE STUPID MISTAKES NOW on the last 100.
	 def bfs(self, parent, s, t):

	 	
	 	q = collections.deque()
	 	visited = [-1] * self.m

	 	q.append(s) # holds vertex indices
	 	

	 	while q:
	 		u = self.q.popleft()
	 		visited[u] = 1

	 		for i, val in enumerate(self.res_graph[u]): # do this in res graph
	 			if not visited[i] and val > 0:
	 				self.q.append(i)
	 				parent[i] = u

	 	return visited[t] == 1

	 def dfs(self, u, graph, visited):
	 	visited[u] = 1
	 	for i, v in enumerate(graph[u]):
	 		if not visited[i] and v > 0:
	 			self.dfs(i, graph, visited)

	 def min_cut(self, s, t):

 		parent = [-1] * self.m # to hold path

 		max_flow = 0 
	 	# while there is a path in agumented graph

	 	while self.bfs(source, sink, parent):

	 		path_flow = float('inf')
	 		
	 		u = sink

	 		while u != source:
	 			path_flow = min(path_flow, self.res_graph[parent[u]][u])  # in max flow net, all edges should have equal inflow and outflow for max flow path; except for to source and sink
	 			u = parent[u] 

	 		max_flow += path_flow

		 	# to max flow; minimize residual capacities through graph edges
		 	u = sink

		 	while u != source:
		 		v = parent[u]
		 		self.res_graph[v][u] -= path_flow # reverse
		 		self.res_graph[u][v] += path_flow
		 		u = parent[u]

	 	# to get min cut do a traversal on final residual graph; 
	 	visited = [0] * self.m
	 	self.dfs(source, self.res_graph, visited)

	 	# edges: if in res_graph are xero and in original were not and were now visited in the res_graph on the max flow path

	 	for row in range(self.m):
	 		for col in range(self.n):
	 			if not self.res_graph[i][j] and self.graph[i][j] and visited[i]:
	 				print(i, j)










