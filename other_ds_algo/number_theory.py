

def pow_mod(x, y, p):
	"""
	Calculate x**y mod p using property
	ab(mod)p = ((a mod p)(b mod p)) mod p

	and y//2 for O(log) x**2 ** y//2

	#  y & 1 != 0 if y odd

	2 ** 3 % 5
	2 % 5 = 2
	(6%5)(6%5)(6%5) mod 5 =  


	"""

	res = 1
	x = x % p # like a mod p
	if x == 0: return 0

	while y > 0:

		if y & 1:
			res = (res * x) % p 

		y = y // 2
		x = (x * x) % p # bc of y // 2



	return res

# print(pow_mod(2, 3, 5))


# Mod inverse (I used this in Fourier work)



def base_euclid_gcd(a, b):
	"""
	b > a: gcd(a, b) = gcd(b%a, a) # think example with factors 
	Called Base Euclid algorithm
	"""

	if a == 0:
		return b

	return base_euclid_gcd(b%a, a)

print(base_euclid_gcd(10, 15))



def get_gcd_extended_Euclid_algo(a, b):
	"""
	Goal: find x, y so that:
	gcd(a, b) = ax, by
	"""
	if  a == 0:
		return b, 0, 1

	gcd, x1, y1 = get_gcd_extended_Euclid_algo(b%a, a) # assume b > a
	print(x1, y1)
	y = x1
	x = y1 - x1 * (b // a)
	return gcd, x, y

print(get_gcd_extended_Euclid_algo(12, 10))

def inverse_mod(a, m):
	"""
	find x so that ax ~= 1 mod m; x is in 0..m-1
	or ax mod m = 1 

	assume gcd(a, m) = 1

	use expanded Euclidean algo: get x, y so that ax + by = gcd(a, b) where b = m

	ax + my = 1 so ax % m = 1 = modular inverse of a is x
	"""
	gcd, x, y = get_gcd_extended_Euclid_algo(a, m)
	print(gcd, x, y)
	return x

# inverse_mod(15, 4)

# Fermat little theorem: probabilistic for primality testing
import random

def is_prime_Fermat(n, k):
	"""
	for a in range[2, n - 2]: a**(n-1) % n = 1

	* use modular eponentian function for O(logn) power calc
	"""
	if n == 4 or n <=1: return False
	if n <= 3: return True

	while k > 0:

		a = random.randint(2, n-2)

		if base_euclid_gcd(a, n) != 1:
			return False

		if get_mod_pow(a, n-1, n) != 1:
			return False
		k -= 1

	return True

print(is_prime_Fermat(6, 3))

# Skip Euler's totient: count of num in {1, .., n-1} reelatively prime to n.: = n prod(1 - 1/p); p prime factors of n
# don't know the proof of this 

def sive_erathostente(n):
	""""
	find all primes <= n
	"""
	nums = [True] * (n+1)

	p = 2
	while p * p <= n:

		if nums[p]:
			for j in range(p*p, n+1, p):
				nums[j] = False
		p += 1

	primes = {i for i,x in enumerate(nums) if x}

	return primes



# Get convex hull: Jarvis's algorithm (march)

# useful ideas: if lines intersect; orientation of 3 points: val = 0 colinear; 1 clockwise

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def orientation(p, q, r):
	val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y) # from slopes comparison
	if val == 0:
		return 0
	return 1 if val > 0 else 2

def jarvis(points):

	# left most

	left = 0

	for i, p in enumerate(points):
		if p.x < points[left].x:
			left = i

	p = left
	hull = []
	q = 0
	while True:
		hull.append(p)

		q = (p + 1) % n

		for i in range(n):
			if orientation(points[p], points[i], points[q]) == 2: # i is more countercloqwise than q from p direction
				q = i 

		if q == p: break
		q = p

	return hull



def segmented_sieve(n):
	"""get all prime numbers between 0 and n with memory savings.

	Idea: split in intervals of length sqrt(n): 0-sqrt(n); sqrt(n)+1, 2*sqrt(n) etc
	- apply simple_eratosthene sieve on intervals using same memory to update primes.

	"""
	def sive_erathostente(num):
		marks = [True] * (num+1)
		if num < 2: return [0, 1]
		p = 2
		while p * p < num:
			if marks[p]:
				for i in range(p*p, num+1, p):
					marks[i] = False
			p += 1
		return [i for i, x in enumerate(marks) if x and i > 2]


	limit = math.ceil(math.sqrt(num))
	primes = sive_erathostente(n)

	low, high = limit, 2 * limit 

	while low <= n:
		if high > n:
			high = n

		marks = [True] * (limit + 1)

		for i in range(len(primes)):

			lowlimit = (low // primes[i]) * primes[i]
			if lowlimit < limit:
				lowlimit += prime[i]

			for j in range(lowlimit, high, primes[i]):
				marks[j-lowlimit] = False

		for i in range(low, high):
			if marks[i-low]:
				print('prime', i)

		low += limit
		high += limit










