'''
Replicable code from interesing and common google problems.

'''

# Linear algebra - geometry approach 
# https://leetcode.com/problems/minimum-area-rectangle-ii/solution/

# Approach 1 using 3 points formin a triangle and then looking for the 4th to form a rectangl
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        
        # complex notation of vector
        points = set(map(tuple, points))
        ans = float('inf')
        EPS = 1e-7
        
        # take any 3 points
        for p1, p2, p3 in itertools.combinations(points, 3):
            # check if the 4th points that would make equal axis projections of the edges exists in points; assume the 3 points have p1 as reference
            p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
            if p4 in points:
                # get edges by complex representation to: get edge/vector length (abs) 
                # check cos or dot prod (inner prod in Euclid space) is 0 (abs() + abs)
                v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
                v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
                
                # check orthogonality: note the dot product in complex repres
                if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
                #     # area is prod of vector length
                    area = abs(v21) * abs(v31)
                    if area < ans:
                        ans = area
        
        
        return ans if ans < float('inf') else 0
# Better approach close to what I had in mind but see radius and center thinking for dictionary key tuple
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = [complex(*z) for z in points]
        
        d = collections.defaultdict(list)
        
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2 # can get the O point directly with both coord
            # print(center)
            radius = abs(center - P) # since center - P is a point or vector with
            # origin at P we want the length of the vector PO so use modulus
            # print(center - P)
            d[center, radius].append(P) # note again the tuple automatically forms key
            # looking for pair of points with the same center and radius 
            
        # then in each group form a rectangle and get min area
        
        ans = float('inf')
        for (center, radius), candidates in d.items():
            # print("center O", center)
            for P, Q in itertools.combinations(candidates, 2):
                # print('P', P, 'Q', Q)
                # Do it again: why do we get the edge length this way
                ans = min(ans, abs(P - Q) * abs(P - (2 * center - Q)))
                
        return ans if ans < float('inf') else 0
        

# Stream of char P 1032 wi trie
class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.trie = {}
        self.dq = collections.deque([])
        
        for word in set(words):
            node = self.trie 
            for ch in word[::-1]: #trie from reversed
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word


    def query(self, letter: str) -> bool:
        self.dq.appendleft(letter)
        node = self.trie
        for ch in self.dq:
            if '$' in node: return True
            if ch not in node: return False
            node = node[ch]
        return '$' in node
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

# Stone Game II P1140


@functools.lru_cache(None)
def memo(start, M, alex_turn):
	if start >= len(piles): return 0
	tot_s = float('-inf')
	for x in range(1, 2*M+1):
		current_pile = sum(piles[i:i+x]) if alex_turn == 1 else 0
		rest_of_game = alex_turn * memo(start+x, max(x,M), -alex_turn)
		tot_s = max(tot_s, current_pile + rest_of_game)

	return alex_turn * tot_s



# P1376 Time to inform all employees clean BFS and DFS with building min graph

def max_time(managers, informTimes, headID):
	subordinates = collections.defaultdict(list)
	for i,m in enumerate(managers):
		subordinates[m].append(i)


	# bfs
	maxT = 0
	q = collections.deque()
	q.append((headID, informTimes[headID]))
	while q:
		current, time = q.popleft()
		max_time = max(time, max_time)
		for subord in subordinates[current]:
			q.append((time+informTimes[subord]))


	return max_time

	#dfs
	def dfs(id):
		time = 0

		for subord in subordinates[id]:
			time = max(time, dfs(subord))

		time += informTimes[id]
		return time
	return dfs(headID)

# good clean stack code for final prices with discount P1475 
# (also a temperatures problem this version is min; that one was similar but max)

def final_prices(prices):
	if len(prices) < 2: return prices
	ans = [x for x in prices]
	stack = []

	for i, x in enumerate(prices):
		while stack and ans[stack[-1]] >= x:
			ans[stack.pop()] -= x
		stack.append(i)
	return ans 


# P 659 split array into consec subsequences - the counter problem pattern
def is_possible(sorted_nums):

	c = collections.Counter(sorted_nums)
	tails = collections.Counter()

	for x in nums:
		if c[x] == 0: continue
		elif tails[x] > 0:
			tails[x] -= 1
			tails[x+1] += 1
		elif c[x+1] > 0 and c[x+2] > 0:
			c[x+1] -= 1
			c[x+2] -= 1
			tails[x+3] += 1
		else:
			return False
		c[x] -= 1
	return True

# P 1477 Find two non-overlapping subarrays each with target sum. (return min of their length sum)

def find_two_sub(arr, target):
	'''dynamic progr'''
	start, s, ans, min_len = 0, 0, float('inf'), float('inf')
	dp = [float('inf')] * len(arr)

	for i, x in enumerate(arr):
		s += x
		while s > target:
			s -= arr[start]
			start += 1

		if s == target and dp[start - 1] < float('inf'):
			curr_len = i - start + 1
			ans = min(ans, curr_len + dp[start-1])
			min_len = min(min_len, curr_len)
		dp[i] = min_len

	return ans if ans < float('inf') else -1

# P837. New 21 game. Calc probab of win: hit N but not higher while rule is to stop at K. draw in [1, w]

def alice_21_dp(N, K, W):
	dp = [0.0] * (N + W + 1)

	for k in range(K, N+1):
		dp[k] = 1.0

	S = sum([dp[K+x] for x in range(1, W+1)])

	for k in reversed(range(K)):
		dp[k] = S * (1.0 / W)
		S = S + dp[k] - dp[k+w]
		
	return dp[0]

# Good 2 pointer code: if two strings are equal after some '#' is the backspace op and delete the
# char before P844
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
                    
        # print(list(F(S)))     
        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


# Burst balloons - given [3, 1, 5, 8]; burst ballon (disappears) and max amount of coins.
# Trick here is the two-side dp calls and the addition to the initial array of left and right
# also notice the dp bottom up mimicing the td so well; Note in dp bottom up, 
# the loops are typically from n down if final result is dp[0] and from 0 up if result is dp[n-1].

# Both sol ar O(n**3), O(n**2) really easily seen in the DP bottom up.


# top down memo solution

def burst_ballons(nums):
	nums = [1] + nums + [1]

	n = len(nums)

	@lru_cache
	def td(left, right):
		if left + 1 == right: return 0

		return max([nums[i] * nums[left] * nums[right] + td(left, i) + td(i, right) for i in range(left + 1, right)])

	return td(left=0, right = len(nums) - 1) # note the nums has the 2 additonal elems

# bottom up corresponding solution

def burst_balloons(nums):
	nums = [1] + nums + [1]

	n = len(nums)
	dp = [[0] * n for _ in range(n)]

	for left in range(n-2, -1, -1):
		for right in range(left+2, n):
			dp[left][right] = max(nums[i] * nums[left] * nums[right] + dp[left][i] + dp[i][right] for i in range(left+1, right)]) # trick is the choice
			# of left and right and i in interval; 

	return dp[0][n-1]
	
