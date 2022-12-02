
# Implementation of union-find data structure basic; initialize to parent to -1 or parent of x is x
"""
* also called disjoint set
* O(N) if naive implementation
* can be used for finind cycles or connected components
* it is used in kruskal
* can have O(logn) on find and union ops if done with path compression and union by rank
"""

class DSU1:
    def __init__(self, n):
        self.par = list(range(n))

    def find(self, x):
        """Find leader of x"""
        while self.par[x] != x:
            x = self.par[x]
        return x

    def union(self, x, y):
        """merge/union leader of x with leader of y if they are distinct; connect two components"""
        xl, yl = self.find(x), self.find(y)
        if xl == yl:
            return False
        self.par[xl] = yl # pick randomly which is set to which in this implementation
        return True


# path compression
class DSU2:
    def __init__(self, n):
        self.par = list(range(n)) # not clear when you set it to -1 and how many
    def find(self, x):
        """with path compression"""
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])

        return self.par[x]

    def union(self, x, y):
        xl, yl = self.find(x), self.find(y)
        if xl == yl:
            return False
        self.par[xl] = yl
        return True


# Further optimize: union by rank is - set the leader of the class with smaller following to the leader with more following


class DSU3:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n 

    def set_par(self, x):
        self.par[x] = x


    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False

        elif self.rank[xr] < self.rank[yr]:
            self.par[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rank[xr] += 1
        return True



"""
Floyd-Warshall Algorithm to solve all pairs shortest path problem.
Find shortest dist between every pair of vertices in given edge weighted directed graph.

- so updates dist[i][j] to dist[i][k] + dist[j][k] if that is smaller for every pair i, j
- to keep path - can hold parents into a 2-d matrix

# initial dist: float(inf) or 0

O(v**3)
"""
V = 4
graph = [[0,5,INF,10], 
             [INF,0,3,INF], 
             [INF, INF, 0,   1], 
             [INF, INF, INF, 0] 
        ] 
def floyd_warshall(graph):
    dist = [[g[i][j] for j in range(V)] for i in range(V)]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


    print(dist)



"""
Djikstra single source shortest path from source to all vertices for graph. Matrix adjacency rep.

Steps:
- initialize vertices dist to infinity. (the dist array that gets updated in the algo)
- initialize source dist to 0.
- create initially empty set for vertices in the set added.
- pick vertex u which is not in initial set and has min dist val. Add it to set.
- iterate through adjacent vertices (to u) v and calculate dist(u) + u-v edge weight. if this 
is < dist(v), update dist(v). 


"""

""""
# djikstra variation with custom weight function
https://leetcode.com/problems/path-with-minimum-effort/solution/
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
       
        m, n = len(heights), len(heights[0])
        diff_mat = [[math.inf] * n for _ in range(m)]
        
        diff_mat[0][0] = 0
        visited = [[False]* n for _ in range(m)]
        
        def get_n(r, c):
            for nr, nc in [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]:
                if 0 <= nr < m and 0 <= nc < n:
                    yield (nr, nc)
        
        pq = [(0, 0, 0)] # diff, x, y
        
        while pq:
            d, x, y = heapq.heappop(pq)
            visited[x][y] = True
            for nr, nc in get_n(x, y):
                if not visited[nr][nc]:
                    curr_diff = abs(heights[x][y] - heights[nr][nc])
                    max_diff = max(curr_diff, diff_mat[x][y])
                    if diff_mat[nr][nc] > max_diff:
                        diff_mat[nr][nc] = max_diff
                        heapq.heappush(pq, (max_diff, nr, nc))
    
        
        return diff_mat[-1][-1]
        



if __name__ =='__main__':
	main()
