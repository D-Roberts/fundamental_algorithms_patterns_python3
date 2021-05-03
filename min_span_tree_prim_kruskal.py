""""
MIn spanning tree Kruskal.

MST: spanning tree(connects all vertices; so has V - 1 edges) of min weight/cost (amid other possible spannign trees).
MST: network design; approximation of NP-hard problem such as travelimg salesman.

Kruskal: Uses union find; Also Greedy

Steps:
1. Sort all vertices in ascending order of weight
2. Pick the one with min weight to include in the mst
3. Check if it forms cycle with the already formed mst
4. If no: include; if yes: discard.
"""


class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.g = []

	def addEdge(self, u, v, w):
		self.g[u].append([u, v, w]) # edges in this graph rep

	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	def union(self, parent, rank, x, y):
		xr = self.find(parent, x)
		yr = self.find(parent, y)
		if rank[xr] < rank[yr]:
			parent[xr] = yr
		elif rank[xr] > rank[yr]:
			parent[yr] = xr
		else:
			parent[xr] = yr
			rank[xr] += 1

	def KruskalMST(self):
		# mst
		mst = []
		parent = [i for i in range(self.V)]
		rank = [0] * self.V

		# sort graph in non-decreasing edge weight
		self.g = sorted(self.g, key=lambda x: x[2]) # by weight # Alternative is heapify

		e, i = 0, 0
		while e < self.V - 1: # num edges in mst; Here may want to use a heap and condition on heap empty
			u, v, w = self.g[i]
			i += 1

			pu, pv = self.find(parent, u), self.find(parent, v)

			# if not cycle
			if pu != pv:
				e += 1 # otw discard
				mst.append([u, v, w])
				self.union(parent, rank, pu, pv)




		# the total cost
		total_cost = sum([w for u, v, w in mst])
		pritn(total_cost)


# A better KRuskal implementation with pq - note here edges are given in list
# instead of total cost we get a min time quantity
# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        
        par = [i for i in range(N)]
        
        heapq.heapify(logs) # edges
        mst = [] # min span tree
        
        def find(u):
            if u != par[u]:
                par[u] = find(par[u])
            return par[u]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu != pv:
                par[pu] = pv
                
       # e = 0
        while logs:
            time, u, v = heapq.heappop(logs)
            pu, pv = find(u), find(v)
            if pu != pv:
                #e += 1
                mst.append([u, v, time])
                union(pu, pv)
                if len(mst) == N-1:
                    return time

        return -1



# Min Span Tree PRIM

"""
Prim's minimum spanning tree MST: Greedy Algo - 5

O(V^2) for adjacency matrix representation. O(ElogV) for binary heap implementation

Algo:
Spanning tree: connects all edges
Minimum: min weight 

Cut in graph: group of edges that connect two sets of vertices in a graph.

At each step of Prim's: pick the min weight vertex from a cut with one set of Vertices: the mst;
# the other set of vertices: not included in MST.
- adds the min vert to the set
 - updates the key/ weoght of the neighbor vertex with the graph edge between the two
 - udpates the parent of the neighbor vertex with the current vertex
"""

# First adjacency matrix implementation from geeks

# use Prim's or Kruskal's for minimum spanning tree (in connected graph)

# see the heap implementation in Python from leetcode; this one does not work but illustrates the algo well.
# https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843995/Python-3-or-Min-Spanning-Tree-or-Prim's-Algorithm

import sys # Library for INT_MAX 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    # A utility function to print the constructed MST stored in parent[] 
    def printMST(self, parent): 
        print ("Edge \tWeight")
        for i in range(1, self.V): 
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ] )

    def min_key(self, key_arr, mst_set):
    	min_k = float('inf')
    	min_ind = 0
    	for v in range(self.V):
    		if mst_set[v] == False and key_arr[v] < min_k:
    			min_ind = v 
    			min_k = key_arr[v]
    	return min_ind

    def prim_mst(self):

    	mst_set = [False] * self.V
    	key = [float('inf')] * self.V 
    	parent = [None] * self.V 

    	key[0] = 0
    	parent[0] = -1

    	for cout in range(self.V):
    		u = self.min_key(key, mst_set)
    		mst_set[u] = True

    	for v in range(self.V):
    		if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
    			parent[v] = u
    			key[v] = self.graph[u][v]

    	self.printMST(parent) # doesn't really work; 



def main():
	g = Graph(9)
	g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]
  
	g.prim_mst()

if __name__ =='__main__':
	main()


#https://leetcode.com/problems/min-cost-to-connect-all-points/submissions/    

# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         def cost(p1, p2):
#             return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
#         n, c = len(points), collections.defaultdict(list)
#         # compute distances from each point to points after it in a directed graph sort of mimicing fashion to avoid cycles
#         for i in range(n):
#             for j in range(i+1, n):
#                 d = cost(points[i], points[j])
#                 c[i].append((d, j))
#                 c[j].append((d, i))
#         # print(c)
#         cnt, ans, heap = 0, 0, [(0, 0)] 
#         # we must see all points so we must keep count    
#         # start with heap with point 0 
#         seen = set()
#         # no points seen
        
#         while heap and cnt < n:
#             d, j = heapq.heappop(heap) # no need to heapify first in this case
#             # first point popped is 0
#             if j not in seen:
#                 cnt, ans = cnt+1, ans+d
#                 seen.add(j)
#                 # next visit connected points and their edge cost
#                 for record in c[j]: heapq.heappush(heap, record) # add all next possibel points and their distance to the current point
            
#         return ans # total cost to visit all points



