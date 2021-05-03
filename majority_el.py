"""
Majority search (elem shows up more than 50% of the time and Majority search 1/k (elem shows up more than n/k of the time);
Boyer-Moore voting algo. O(n); O(1) or O(k)
"""
import collections

def majority(nums):
	if nums is None: return None
	candidate, count = nums[0], 0

	for num in nums:
		if num == candidate: count += 1
		elif count > 0: count -= 1
		else:
			candidate = num
			count = 1
	count = 0
	for num in nums:
		if candidate == num:
			count += 1
	n = len(nums)
	return candidate if count > n // 2 else None 

def majority_k(nums, k):
	d = collections.defaultdict(int)
	if not nums: return None
	for num in nums:
		d[num] += 1
		if len(d.keys()) == k:
			for key in list(d.keys()):
				d[key] -= 1
				if not d[key]: del d[key]
	# # keep the keys reset the count

	for key in d.keys():
		d[key] = 0
	for num in nums:
		if num in d.keys(): 
			d[num] += 1
	for key in d.keys():
		if d[key] > len(nums)/k:
			return key
	return None

def main():
	a = [4, 2, 3, 3, 5, 6]
	# sometimes it cannot be not found	
	# print(majority(a))
	print(majority_k(a, 3))
if __name__ == '__main__':
	main()
