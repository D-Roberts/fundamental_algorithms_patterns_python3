"""
Heaps. O(1)

"""
import collections

def find_smallestk(nums):
	# arr = [ 4, 2, 8, 1]

	# [-4, -2, -1] # min heap of neg is max heap [4, 2, 1]
	# say [-8, -2, -1] and come accross 4; [-8, -4, -2, -1]; [-4, -2, -1]
	pq = []

	for x in arr:
		if len(pq) >= k and x < -pq[0]:
			heapq.heappushpop(pq, -x)

		elif len(pq) < k:
			heapq.heappush(pq, -x)

	return -pq[0]

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here. Streaming data median.
        """
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        

    def findMedian(self) -> float:
        return -self.left[0] if len(self.left) > len(self.right) else 0.5 * (-self.left[0] + self.right[0])
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def is_overlap(inputs):
	line = []
	for i, interval in enumerate(input):
		line.append((interval[0], 'start'))
		line.append((interval[1], 'end'))

	line.sort()

	for t in line:
		if t[1] == 0:
			count += 1
		else:
			count -= 1
			if count > 0:
				return True
	return False


def merge_intervals(intervals):
	line, out = [], []
	for interval in intervals:
		line.append((interval[0], '0')) # start
		line.append((interval[1], '1')) # end
	line.sort(key = lambda x: (x[0], x[1]))
	print(line)
	count = 0
	for t, se in line:
		if se == '0':
			count += 1
			if count == 1:
				current_start = t 
		else:
			count -= 1
			if not count:
				out.append((current_start, t)) #just ended a merged interval

	return out


def skyline(buildings): #(L,R, H)
	line = [(L, -H, R) for L, R, H in buildings] + list(set([(R, 0, 0) for _ , R, _ in buildings]))

	out, pq = [[0, 0]], [(0, float('inf'))] # pq init to (heigh=0, right=floatinf)

	for L, nh, R in sorted(line):
		while pq[0][1] <= L: # ending buildings
			heapq.heappop(pq)
		if nh != 0: heapq.heappush(pq, (nh, R)) # new building as candidate
		if out[-1][1] != -pq[0][0]: # the tallest current building forms outline
			out.append([L, -pq[0][0]])  # only add change of height

	return out[1:]

def heap_sort(arr):
	# max heap; binary heap in array reepresentation
	# works

	n = len(arr)
	def _heapify(n, i):
		largest = i
		left, right = 2*i + 1, 2 * i + 2

		if left < n and arr[largest] < arr[left]:
			largest = left
		if right < n and arr[largest] < arr[right]:
			largest = right

		if largest != i:
			arr[largest], arr[i] = arr[i], arr[largest]

			_heapify(n, largest)



	# build max heap
	for i in range(n//2 - 1, -1, -1):
		_heapify(n, i)

	# extract elem; max is at 0
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		_heapify(i, 0)

# min heap
# O(logn) decrease key extract mean heapify delete key insert
class Heap:
	def __init__(self):
		self.a = []

	def heapify(self, i):
		"""heapifies at node i; assumes subtrees are heapified already"""
		smallest, n = i, len(self.a)
		left, right = 2 * i + 1, 2 * i + 2

		if left < n and self.a[left] < self.a[smallest]:
			smallest = left

		if right < n and self.a[right] < self.a[smallest]:
			smallest = right

		if i != smallest:
			self.a[smallest], self.a[i] = self.a[i], self.a[smallest]
			self.heapify(i)

	def delete(self, i):
		self.decrease_key(i, -math.inf)
		self.extract_min()

	def extract_min(self): # it removes it from the heap
		"""swap first with last and heapify first"""
		n = len(self.a)
		if n == 0:
			return math.inf
		if n == 1:
			root = self.a[0]
			self.a = []
			return root

		root = self.a[0]
		self.a[0] = self.a[-1] # the idea to put last first, pop and heapify
		self.a.pop()
		self._heapify(0)

	def parent(self, i):
		return (i - 1) // 2

	def decrease_key(self, i, val):
		"""this is modify/update key; increase though makes no change;
			this is propagate change
		"""

		self.a[i] = val
		while i and self.a[parent(i)] > self.a[i]:
			self.a[i], self.a[parent(i)] = self.a[parent(i)], self.a[i]
			i = parent(i)

	def insert(self, val):
		"""put at the back and propagate up"""
		self.a.append(val)
		i = len(self.a) - 1

		while i and self.a[self.parent(i)] > self.a[i]:
			swap()
			i = parent(i)


def main():
	s = 'abacda'
	
	
if __name__ == '__main__':
	main()
