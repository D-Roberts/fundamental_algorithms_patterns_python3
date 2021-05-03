
import collections

"""
Copy each even element twice. Assune there is room at the back in the array.
Traversal in reverse techinuq.

ESTCV
"""
import collections

def traverse(nums):
	if not nums: return 
	n = len(nums)
	length = n - 1
	
	while length >= 0 and nums[length] == -1:
		length -= 1

	i = n - 1
	while length >= 0:
		if not nums[length] % 2 == 0:
			nums[i] = nums[length]
			i -= 1
		nums[i] = nums[length]
		length -= 1
		i -= 1


"""
Prefix sum. Subarray sums to value target. Neg nums are possible. Not sorted. Think middle of array.
"""

def prefix(nums, target):
	if not nums: return None

	d = collections.defaultdict()
	curr_s = 0
	for i, x in enumerate(nums):
		curr_s += x
		if curr_s == target:
			return (0, i)
		elif curr_s - target in d.keys():
			return (d[curr_s - target] + 1, i)
		d[curr_s] = i
		
	return None


"""
Contig subarray max sum. Can have neg
"""
import collections

def kadane(nums):
	if not nums: return None

	max_s_to_here, maxs = nums[0], nums[0]
	
	for x in nums[1:]:
		max_s_to_here = max(max_s_to_here + x, x)
		maxs = max(maxs, max_s_to_here)

	return maxs

# ANdt hte nlogn variation (P1235: schedule jobs for max profit)
def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # combine timeline with dp (with bin search)
        n = len(profit)
        line = list(zip(startTime, endTime, profit)) # need to sort by end time
        line.sort(key=lambda x: x[1])
        print(line)
        dp = [0] * n
        dp[0] = line[0][2]
    
        for i in range(n):
            prev_profit = 0
            left, right = 0, i - 1
            
            while left <= right:
                mid = (left + right) // 2
                if line[i][0] < line[mid][1]: # need prev job to end bef current
                    right = mid - 1
                else:
                    prev_profit = dp[mid]
                    left = mid + 1
            dp[i] = max(dp[i-1], prev_profit + line[i][2])
    
        return dp[-1]
            
            


#dnf

def dnf(nums, pivot):
    i, lb, hb = 0, 0, len(nums) - 1
    while i <= hb:
        if nums[i] < pivot:
            nums[i], nums[lb] = nums[lb], nums[i]
            lb += 1
            i += 1
        elif nums[i] > pivot:
            nums[i], nums[hb] = nums[hb], nums[i]
            hb -= 1
        else:
            i += 1

"""
Two sum for sorted array with pos elem. Traverse from both ends technique.
"""            

def two_sum_sorted_pos(nums, target):
	i, j = 0, len(nums) - 1
	ans = None
	while i != j:
		s = nums[i] + nums[j]
		if s == target:
			ans = (i, j)
			break
		elif s < target:
			i += 1
		else:
			j -= 1
	return ans


"""
Two pointer. Subarray sums to value target.Pos numbers only. Qualifies for a "greedy" approach.
"""
import collections

def two_pointer(nums, target):
	if not nums: return None

	start, end, curr_s = 0, 0, nums[0]

	while start < len(nums):
		if start > end:
			end = start
			curr_s = nums[start]
		if curr_s < target:
			if end == len(nums) - 1: break
			end += 1
			curr_s += nums[end]
		elif curr_s > target:
			curr_s -= nums[start]
			start += 1
		else:
			return (start, end)
		
	return None

# Better python code for two pointer solution for example in https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/submissions/
# which gets the longeest subarray sums up to nx (equivalent to min ops at ends to sum to x)
# class Solution:
    def two_pointer_minOperations(self, nums: List[int], x: int) -> int:
        """trick: longest sub sums up to total - x"""
        nx = sum(nums) - x
        n = len(nums)
        
        start, end, maxlen, s = 0, 0, -1, 0
        
        for end in range(n):
            s += nums[end]
            while s > nx and start <= end:
                s -= nums[start]
                start += 1
            if s == nx:
                maxlen = max(maxlen, end - start + 1)
                
            
        return n - maxlen if maxlen != -1 else -1



"""
Two pointer. Longest substring with unique characters.
!Note to self: thrink through the algorithm assuming you are "in the middle of processing".
Then think through what happens at the beginning and then at the end.
"""

def two_pointer(s):
	# "whatwhywhere" --> "atwhy"
	pair_s, pair_e = None, None
	start, end, max_len = 0, 0, 1
	d = collections.defaultdict(int)
	d[s[0]] = 0

	while end < len(nums) - 1:
		end += 1
		to_add = s[end]
		if to_add in d.keys() and d[to_add] >= start:
			start = d[to_add] + 1
		d[to_add] = end
		if end - start + 1 > max_len:
			pair_s, pair_e = start, end
			max_len = end - start + 1

	return (pair_s, pair_e)


"""
Determine contig subarray which if sorted leads to entire array being sorted. 

Steps:
- progress two pointers from start and end
- from start to where elem increasing seq stops
- from back where elems decreas order stops
- return indeces where subarray starts and ends

"""


def sorted_subarray(nums):
	i, j = 0, len(nums) - 1
	
	while i < len(nums) - 1 and nums[i+1] > nums[i]:
		i += 1
	print(i)

	if i == len(nums) - 1:
		return None

	while j > 0 and nums[j] > nums[j-1]:
		j -= 1
	print(j)

	minn, maxn = min(nums[i:j]), max(nums[i:j])
	print(minn, maxn)
	while i > 0 and nums[i - 1] > minn: #TODO: indeces not quire right where j lands
		i -= 1
	# the i and j are currently included in the middle; actually j is not; j - 1 is
	# but i is
	while j < len(nums) - 1 and maxn > nums[j+1]:
		j += 1

	return (i, j)


    

def main():
	s = 'abacda'
	a = [1, 2, 3, 4]
	
	print(two_sum_sorted_pos(a, 6))
	

	
if __name__ == '__main__':
	main()
