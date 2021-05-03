"""
Sorts

"""

def selection_sort(a, k):
	'''find the kt order stat; alternative to sort min heap max heap'''
	def partition(a, rand_ind, start, end):
		'''visualize cloud'''
		a[start], a[rand_ind] = a[rand_ind], a[start]
		less = start 
		for i in range(start+1, end+1):
			if a[i] <= a[start]:
				a[i], a[less] = a[less], a[i]
				less += 1

		a[start], a[less] = a[less], a[start]
		return less 

	def _sel(a, target_ind, start, end):
		rand_ind = random.randint(start, end)
		pivot_ind = partition(a, rand_int, start, end)
		if pivot_ind == target_ind:
			return a[target_ind]
		elif pivot_ind > target_ind: 
			return _sel(a, target_ind, start, pivot_ind - 1)
		else:
			return _sel(a, target_ind, pivot_ind+1, end) # I am not clear that this works

	return _sel(a, k-1, 0, len(a)-1)

def merge_sort(a):
	if len(a):
		mid = len(a) // 2
		L = a[:mid]
		R = a[mid:]
		merge_sort(L)
		merge_sort(R)
		i, j = 0, 0
		res = []
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				res.append(L[i])
				i += 1
			else:
				res.append(R[j])
				j += 1
		while i < len(L):
			res.append(L[i])
			i += 1
		while j < len(R):
			res.append(R[j])
			j += 1
		a[:] = res

# External sort: sorting large data: diagram and how to use stable sort.

def quick_sort(a):
	if not a: return a
	_qs(0, len(a)-1)
	

	def _qs(start, end):
		if start < 0 or end > len(a) or start >= end:
			return
		pivot_ind = random.randint(start, end)
		points = get_dnf(start, end, pivot_ind)
		_qs(start, points[0])
		_qs(points[1], end)

def get_dnf(a, start, end, pivot_ind):
	pivot = a[pivot_ind]
	low, high, mid = start - 1, end + 1, start - 1

	while mid+1 < high:
		if a[mid+1] > pivot:
			a[mid+1], a[high] = a[high], a[mid+1]
			high -= 1
		elif a[mid+1] == pivot:
			mid += 1
		else:
			a[mid+1], a[low+1] = a[low+1], a[mid+1]
			mid += 1
			low += 1
	return [low, high]

# sorts

def count_sort(a):
	# if range a[i] is in finite range(i) O(n+k) if el in [0, k]

	m = max(a)

	count = [0] * (m+1)
	res = [0] * len(a)

	for i, x in enumerate(a):
		count[x] += 1

	for i in range(1, m+1):
		count[i] += count[i-1]

	for i in range(len(a)):
		res[count[a[i]]-1] = a[i]
		count[a[i]] -= 1

	a[:] = res

nums = [5, 4, 2, 8, 2]
# count = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# count = [0, 0, 2, 0, 1, 1, 0, 0, 1]
# count_inc = [0, 0, 2, 2, 3, 4, 4, 4, 5] 
# = [2, 2, 4, 5, 8] []


def radix_sort(a):
	"""O(n) if len(max) = log2(n). Starts at last digit: 802 starts at 2, then 0 .."""

	m = max(a)

	def _count_sort_helper(a, exp):
		n = len(a)
		count = [0] * 10
		res = [0] * n
		curr_arr = [(a[i]//exp) % 10 for i in range(n)]
		print('curr_arr', curr_arr)
		for i, x in enumerate(curr_arr):
			count[x] += 1

		for i in range(1, 10):
			count[i] += count[i-1]

		for i in reversed(range(n)): # must start from back to be stable
			res[count[curr_arr[i]] - 1] = a[i]
			count[curr_arr[i]] -= 1
		a[:] = res


	exp = 1
	
	while m // exp > 0:
		_count_sort_helper(a, exp)
		exp *= 10
	

nums = [1, 289, 45, 78, 6]
# [1, 45, 6, 78, 289]

radix_sort(nums)
# 
def bucket_sort(a):
	"""For a large num of float numb in range 0, 1 uniformly distributed in the range."""

	def _insert_sort(b):
		for i in range(1, len(b)):
			up = b[i]
			j = i - 1
			while j >= 0 and b[j] > up:
				b[j+1] = b[j]
				j -= 1
			b[j+1] = up
		return b
		
	
	slot_num = 10
	arr = [[] for _ in range(slot_num)]

	for x in a:
		ind = int(10 * x)
		arr[ind].append(x)
		# print(arr[ind])

	res = []
	for bucket in arr:
		bucket[:] = _insert_sort(bucket)

	for bucket in arr:
		res.extend(bucket)
	nums[:] = res

            


def main():
	a = [ 1, 3, 4, 4, 5, 6, 5]
	
	
if __name__ == '__main__':
	main()
