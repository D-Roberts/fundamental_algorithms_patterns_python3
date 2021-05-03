"""
Graphs.

"""
"""
Find value in graph via dfs.
"""

import collections


def dfs_find(lis_of_lis, val):
	if not lis_of_lis:
		return False
	graph = collections.defaultdict(set)

	for node, nei in enumerate(lis_of_lis):
		print(nei)
		for n in nei:
			graph[node].add(n)
			if n not in graph:
				graph[n] = set()

	def _dfs(node, visited):
		print(node)
		if node == val:
			return True
		visited.add(node)
		return any(graph[n] not in visited and _dfs(n, visited) for n in graph[node])


	print(graph)
	visited = set()
	
	return any(k not in visited and _dfs(k, visited) for k in graph)

# TODO: test clone_graph

 def clone_graph(g):
 	from copy import deepcopy

 	def dfs_visit(node, g, g_clone, state, visited):
 		for n in g[node]:
 			if n not in state:
 				new_n = deepcopy(n)
 				state[n] = new_n
 			g_clone[state[node]].add(g_clone[state[n]]) # add neighbors in all cases this is the main trick
 			if n not in visited:
 				dfs_visit(n, g, g_clone, state, visited)
 		visited.add(node)

 	for node in g.keys():
 		if node not in state:
 			new_node = deepcopy(node)
 			state[node] = new_node
 			dfs_visit[node]

 	return g_clone

 def print_bfs_in_level_from_start(g, start):
 	visite = set()
 	q = collections.dequeu()
 	q.append(start)
 	while q:
 		current = q.popleft()
 		print(current)
 		visited.add(current)
 		for n in g[current]:
 			if n not in visited:
 				q.append(n)
 		

 def word_ladder(start, end, vocab):
 	'''Return shortest path one letter at a time'''

 	if start not in vocab or end not in vocab or len(start) != len(end):
 		return 0
 	combos = collections.defaultdict(list)
 	L = len(start)
 	for word in vocab:
 		for i in range(L):
 			combos[word[:i] + '*' + word[i+1:]].append(word)

 	q = collections.deque()
 	visited  = {start:True}
 	q.append((start, 1))
 	while q:
 		current, level = q.popleft()
 		for i in range(L):
 			interm_w = current[:i] + '*' + current[i+1:]
 			for word in combos[interm_w]:
 				if word == end:
 					return level + 1
 				if word not in visited:
 					visited[word] = True
 					q.append((word, level + 1))

 			combos[interm_w] = [] # this is a trick
 	return -1


def topo_sort(g):
	stack, state = [], collections.defaultdict(int)

	def dfs_visit(node):
		state[node] = 1
		for n in g[node]:
			if not state[n]: # notee here 
				dfs_visit(n)
		state[node] = 2
		stack.append(node)

	for node in g:
		if state[node] != 2: dfs_visit(node)

	return stack 

# get graph diameteere (longest path)
# topo sort + dp
# dp formula: len_path_to_child = max(len_path_to_parents) + 1 # more then one parent

def graph_diameter(input:List[List[]]) -> int:
	g_children = collections.defauldict(dict)
	for i,n in enumerate(input):
		for c in n:
			g[i]['children'].add(c)
		g[i]['l_path'] = 1 
	g_parents = defaultdict(set)
	for i, n in enumerate(input):
		for c in n:
			g[c].add(i)

	stack = deque()

	top_sort(input, stack)
	max_len = 1

	while stack:
		current = stack.popleft()
		curr_max = 1
		for p in g_p[current]:
			curr_max = max(curr_max, g_c[p][len_p])

		g_c[current]['len_p'] = curr_max + 1
		max_len = max(max_len, curr_max + 1)

	return max_len

def top_find_if_cycle(g):
	d_state= defaultdict(int)
	for node in g:
		if d_state[node] == 0 and has_cycle(node):
			return True

	return False

	def has_cycle(node):
		d_state[node] = 1
		for n in g[node]:
			if d_state[n] == 0 and has_cycle(n):
				return True
			elif d_state[n] == 1:
				return True
		d_state[n] = 2
		retunr False

def graph_is_bipartite(g):
	res, bluese = [], []
	d = dict()

	def get_groups(node):
		q = collections.deque()
		c_r, c_b = [], []
		q.append(node)
		d[node][state] = 1
		d[node][level] = 0

		while q:
			curr = q.popleft()
			if d[current][level] % 2 == 0:
				cr.append(current)
			else: cb.append(current)

		for n in graph[current]:
			if d[n][state] == 0:
				q.append(n)
				d[n][state] = 1
				d[n][level] = d[current][level] + 1
			elif d[n][level] == d[node][level]: return (None, None)
		return (cr, cb)

	for node in g:
		if d[node][state] == 0:
			c_red, c_blue = get_groups(node)
			if not c_red and not c_blue: return None 
		else: 
			reds.extend(c_red); blues. extend(c_blue)

	return (reds, blues)

#O(V+E); O(V) typically.

def connected_components(g):
	state = {}
	color = 0

	def dfs(node):
		state[node] = 1
		for n in g[node]:
			if not state[n]:
				dfs(n)
				
	for node in g:
		if not state[node]:
			colors += 1
			dfs(node)
	return colors 


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
                
   
        while logs:
            time, u, v = heapq.heappop(logs)
            pu, pv = find(u), find(v)
            if pu != pv:
            
                mst.append([u, v, time])
                union(pu, pv)
                if len(mst) == N-1:
                    return time

        return -1


def main():
	s = 'abacda'
	
	
if __name__ == '__main__':
	main()
