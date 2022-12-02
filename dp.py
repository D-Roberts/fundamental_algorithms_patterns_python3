"""Dp td and tabulation implementations

"""
import collections



# top down dp
 def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def memo(new_s):
            if new_s == '':
                return True
            return any(new_s[:j+1] in wordDict and memo(new_s[j+1:]) for j in range(len(new_s)))
        
        return memo(s)
        
def fib_memo(n, d):
	if n == 1 or n == 2: return 1
	if n in d.keys(): return d[n]
	result = fib_memo[n-1, d] + fib_memo[n-2, d]
	d[n] = result
	return result

def dp_bot_up_climb_stairs(n):
	dp = [0] * (n + 1)
	dp[0] = 1

	for i in range(n+1):
		if i+1 <= n:
			dp[i+1] += dp[i]
		if i+3 <= n:
			dp[i+3] += dp[i]
		if i+5 <= n:
			dp[i+5] += dp[i]
	return dp[n]

def dp_top_down_stairs_climb(n):
	dp = [0] * (n+1)
	dp[0] = 1
	for i in range(1, n+1):
		min1 = dp[i-1] if i-1 >0 else 0
		min3 = dp[i-3] if i-3 > 0 else 0
		min5 = dp[i-5] if i-5 > 0 else 0
		dp[i] = min1 + min3 + min5
	return dp[n]

def longest_increasing_subseq(nums):
	dp = [1] * len(nums)

	for i in range(len(nums)):
		for j in range(len(nums[:i])):
			if nums[j] < nums[i]:
				dp[i] = max(dp[i], dp[j] + 1)

	return max(dp)

def dp_coin_change_1(coins, target):
	dp = [0] * (target + 1)
	dp[0] = 1
	for c in coins:
		for s in range(c, target+1): # this ensures no duplicates in final number of combinations
			dp[s] += dp[s-c]

	return dp[target]


# DP problem types and solutions
# https://leetcode.com/discuss/general-discussion/662866/dp-for-beginners-problems-patterns-sample-solutions

# top down dp - how to try the current element or not
# problem: can partition in two subsequences with equal sum
 def canPartition(self, nums: List[int]) -> bool:
        # do a top down
        # target1 - target2 = 0
        #dp
        '''
        total = 11 + 11 = 22; 
        if it can: sum would be 11.
        # find subset that sum to 11. 
        # do top down first
        '''
        target = sum(nums) / 2
        if int(target) != target: return False
        
        @functools.lru_cache(None)
        def backt(s=0, i=0):
            # print(s)
            if s == target:
                return True
           
            for j, x in enumerate(nums[i:]):
                if x <= target:
                    return backt(s+x, i+1) or backt(s, i+1)
                
            return False
                
        return backt()
            


def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # backtracking solution
        @functools.lru_cache(None)
        def backtracking(new_target=target):
            if new_target == 0:
                return 1
            ways = 0
            for i, x in enumerate(nums):
                if x <= new_target: 
                    ways += backtracking(new_target - x)
            return ways
            
        return backtracking()

# OR combination sum IV
		n = len(nums)
        @lru_cache(None)
        def td(curr):
            if curr > target: return 0
            if curr == target:
                return 1
            res = 0
            for i in range(n):
                res += td(curr+nums[i])
            return res
        
        
        return td(0)
# ------------------------------
# good sol
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solution/

 def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, s = len(nums), sum(nums)
        target, rem = divmod(s, k)
        if rem or max(nums) > target: return False
        
        dp_size = 1 << n
      
        dp = [-1] * dp_size
        dp[0] = 0

        for mask in range(dp_size):
            if dp[mask] == -1: continue
            for i, x in enumerate(nums):
                if (not(mask & (1 << i))) and dp[mask] + nums[i] <= target:
                    dp[mask | (1 << i)] = (dp[mask] + nums[i]) % target
                    
        # print(dp)
        return dp[-1] == 0


# get longest chain of words one letter appart P 1048

def longest_chain()
	#similar to longest increasing subsequence except precedence of words frunction
	def precede(w1, w2):
		if len(w2) - len(w1) != 1: return False
		l1, l2 = 0, 0
		while l1 < len(w1) and l2 < len(w2):
			if w1[l1] == w2[l2]:
				l1 += 1
				l2 += 1
			else:
				l2 += 1
			if l2 > l1 + 1: return False
		return True


# Partition subset
# 1049. Last Stone Weight II

# stone weight: y-x and none or none and none if x == y return min stone weight or 0
# the +; - idea

# key insight how this transforms into 2 partitions with min difference between the two subset sums:
# because say (y1 - x1) - (y2 - x2) is an array [y1, x1, y2, x2] at first pass we get
# [y1 - x2, y2 - x2]; then at second pass we get the diff of the 2 elem; but rearange terms
# to get (y1 + x2) - (x1 + y2): which is two partitions; sum up and get the difference
# if the sums are equa then 0; so if a subsum = target // 2 then the mindiff is 0 overall 
# the closer the subsum to target // 2 the smaller the difference; because if p1 has subsum sp1; then p2 has subsum (target - sp1)

# one brute force dp
def last_stone(stones):

	values = {stones[0], - stones[0]}
	for x in stones[1:]:
		temp1 = {y - x for y in values}
		temp2 = {y + x for y in values}
		values = temp1.union(temp2)

	return min([v for v in values if v >= 0])

# a dfs solution

 def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        Main tricks here are to notice that
        1. Given stones = [y1, y2, x1, x2], let's assume we pick y1 - x1 and y2 - x2 in a first pass. The new stones array is [y1-x1, y2-x2] assuming that x1 and x2 vanished. Then in the second pass, we do (y1 - x1) - (y2 - x2) to get the final answer. Note that we can re-write: (y1 - x1) - (y2 - x2) as (y1 + x2) - (y2 + x1).
We now notice that what we want is two subarrays of stones that have minimum difference between their sums: min(sp1 - sp2)

        2. Now note that we can write target = sum(stones) = sp1 + sp2. We can further write the min objective min(sp1 - sp2) = min((sp1 + sp2) - (sp2 + sp2)) = min(target - 2*sp2). What value of sp2 will minimize this objective? sp2 = target // 2. So if we can partition the initial stones array into two subarrays of equal sum target // 2, then the final answer is the min = 0. If this partitioning is not possible, partitioning so that sp2 is as close to target // 2 as possible will do.
        
        
        3. Basically we can re-write the min objective min(target - 2 * sp2) = max(sp2) with constraint sp2 <= target // 2
        
        '''
        target = sum(stones)
        dp = [0] * (target // 2 + 1)
        
        for stonew in stones:
            for partition_sum in range(target // 2, 0, -1):
                if partition_sum >= stonew:
                    dp[partition_sum] = max(dp[partition_sum], dp[partition_sum - stonew] + stonew)
                    
        return target - 2* dp[target // 2]

# DP 2d (1d with space optimization); 
# Get the number of distinct subsequences in S that equal T.

# Trick is to: come from the back; recognize that if character i in S does not match character j in T
# we need to move forward whatever result is present at character j in T (because maybe a subs is formed wiht some other char in S that is not i)
# so dp[i][j] = dp[i+1][j]
# and then if characters at i and j in s and t respectivelly are same; the result must be added as well (the opportunity of forming subs with what
# can be formed from i+1, j+1 on. 

def unique_subs(s, t):
	m, n = len(s), len(t)

	@lru_cache(None)
	def td(i, j):
		if j == n: return 1
		if i == m and j < n: return 0

		res = td(i+1, j)
		if s[i] == t[j]:
			res += td(i+1, j+1)
		return res
	return td(0, 0)

# to switch to bottom up: can do dp 1D but easier to think on dp 2D; add a column with 1 to mimic this base case j == 1
# the tricks for the bottom up: mimic the recursion calls and return dp[0][0] coming from m, n down; 
# make dp of size m+1 and n+1; 
# larget s and index i and size m is at row level.
# to know that you must loop back from m, n down to zero; think of dp subsequences: get result at step i-1, j-1 byt thinking of s[i:m] to t[j:n]
# note in recursion - call of td(0, 0) so mimic to return dp[0][0]

m, n = len(s), len(t)
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m+1):
	dp[i][n] = 1

for i in range(m - 1, -1, -1):
	for j in range(n - 1, -1, -1):
		dp[i][j] = dp[i+1][j]
		if t[j] == s[i]:
			dp[i][j] += dp[i + 1][j + 1]
return dp[0][0]






def main():
	s = 'abacda'
	
	
if __name__ == '__main__':
	main()
