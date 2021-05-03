"""
Bin s

"""
import collections

def bin_s(nums, target):
	if not nums: return -1

	low, high = 0, len(nums) - 1

	while low <= high:
		mid = (low + high) // 2
		if nums[mid] < target:
			low = mid + 1
		elif nums[mid] > target:
			high = mid - 1
		else:
			return mid
	return -1
    

def insert_in_order(nums, target):
	low, high = 0, len(nums) - 1

	while low <= high:
		mid = (low + high) // 2
		if nums[mid] <= target:
			if mid == len(nums) - 1: 
				return len(nums)
			low = mid + 1
		else:
			if mid == 0 or nums[mid - 1] < target:
				return mid
			high = mid - 1

def bin_s_du_first(nums, target):
	low, high = 0, len(nums) - 1
	while low <= high:
		mid = (low + high)//2
		if target < nums[mid] or (target == nums[mid] and mid > 0 and nums[mid - 1] == target):
			high = mid - 1
		elif target > nums[mid]:
			low = mid + 1
		else:
			return mid 

def record_and_move_on(a, t): 
	low, high, res = 0, len(a), -1

	def helper(mid, res, a, t):
		if res == -1 or abs(a[mid] - t) < abs(a[res] - t):
			return mid
		return res 

	while low <= high:
		mid = (low + high) // 2
		res = helper(mid, res, a, t)
		if a[mid] < target:
			low = mid + 1
		elif a[mid] > target:
			high = mid - 1

		else: return mid # 

	return res 

def min_rotated_array(a):
	l, h, right = 0, len(a) - 1, a[len(a) - 1]

	while l <= h:
		mid = (l + h) // 2
		if a[mid] <= right and (mid == 0 or a[mid - 1] > a[mid]):
			return mid 

		elif a[mid] > right:
			low = mid + 1
		else:
			high = mid - 1

def search_unknown_size(a, t):

	def find_last_ind(a, low, high):
		while low <= high:
			mid = (low + high) // 2
			try:
				temp = a[mid]
			except IndexError:
				high = mid - 1
				continue
			try:
				temp = a[mid + 1]
			except IndexError:
				return mid
			low = mid + 1
		return -1

	def bin_s_val(a, low, high):
		'''regular bin search'''
		pass

	high, last_ind = 1, -1

	while True:
		try:
			temp = a[high]
		except IndexError:
			last_ind = find_last_ind(a, high//2, high)
			break
		high *= 2
	return bin_s_val(a, t, 0, last_ind)

def find_one_peak(a):
	l, h = 0, len(a) - 1
	while l <= h:
		mid = (l + h) // 2
		left = float('-inf') if mid == 0 else a[mid-1]
		right = float('-inf') if mid == len(a) - 1 else a[mid+1]
		if right < a[mid] < left: high = mid - 1
		elif left < a[mid] < right: low = mid + 1
		elif left > a[mid] < right: high = mid + 1
		else: return mid 
	
	return -1

def main():
	s = 'abacda'
	arr = [1, 2, 3]
	print(bin_s(arr, 3))
	
	
	
if __name__ == '__main__':
	main()
