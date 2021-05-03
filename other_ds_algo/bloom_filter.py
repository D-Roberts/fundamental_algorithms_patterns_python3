
import math
import mmh3
from bitarray import bitarray

class BloomFilter:
	def __init__(self, p, n):
		"""p = false pos ratee = exists if does not; no false negativees (generate exisiting username
			k hash functions; size of bit array for given p = -m*ln(P)/(log2**2)
			false pos come from collisions. n = num of items to encode (usernames for eg)
		"""

		self.m = - (n* math.log(p))//math.log(2)

		self.p = p
		self.n = n 
		self.k = (m * math.log(2)) // n

		self.bitarray = bitarray(self.m)
		self.bitarray.set_all(0)

	def add(self, item):
		digests = []

		for i in range(self.k):
			digest = mm3.hash(item, i) % self.m
			digests.append(digest)

		for digest in digests:
			self.bitarray[digest] = True

	def check(self, item):
		# exist with probab ..

		for _ in range(self.m):
			digest = mm3.hash(item, i)
			if self.bitarray[digest] == 0:
				return False 

		return True