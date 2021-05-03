


import math

divmod( 4, 3)

math.gcd(4, 6)

def fib(n):
	a, b = 1, 1
	while True:
		yield a
		a, b = b, a + b
	
def gen_ab():
	yield('a')
	yield('b')

def ati_gen(begin, step, end=None):
	result = type(begin + step)(begin)
	forever = end is None
	index = 0
	while forever or result < end:
		yield result
		index += 1
		result = begin + step * index

import itertools
import operator

def vowel(c):
	return c.lower() in 'aeiou'


def main():
	# for c in gen_ab():
	# 	print (c)

	# for d in fib(4):
		# print(d)

	# for el in ati_gen(3, 2.0, 300):
	# 	print(el)


	# itertools and functools 

	# filter generatro functions 

	#1. filter
	print(list(filter(vowel, 'Denisa')))

	#2. compress
	print(list(itertools.compress('Denisa', (1, 0, 1, 0, 1, 0))))

	#dropwhile
	print(list(itertools.dropwhile(vowel, 'enisa')))

	#filterfalse
	print(list(itertools.filterfalse(vowel, 'Denisa')))

	#isslice
	print(list(itertools.islice('Denisa', 2, 4, 1))) # lazy; from any iterable; like [:2]

	#takewhile
	print(list(itertools.takewhile(vowel, 'enisa')))

	# Mapping generator functions
	sample = [5, 4, 2, 8, 7, 6, 3]
	print('acc', list(itertools.accumulate(sample)))
	print(list(itertools.accumulate(sample, min)))
	print(list(itertools.accumulate(sample, max)))
	
	print(list(itertools.accumulate(range(1, 11), operator.mul)))

	print(list(enumerate('Denisa', 2)))

	print(list(map(operator.mul, range(1, 3), range(1, 3)))) # can be several iterators

	#startmap applies function to iterable iterator
	print(list(itertools.starmap(operator.mul, enumerate('Denisa', 1))))

	# running average
	print(list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))))

	# merging generators

	# sequentially
	print(list(itertools.chain(enumerate('Denisa'), 'Denisa')))

	print(list(itertools.chain(enumerate('Denisa'))))
	print(list(itertools.chain.from_iterable(enumerate('Denisa'))))

	# in parallel
	print(list(zip('Denisa', 'Denisa')))
	print(list(itertools.zip_longest('ABC', range(1, 5), fillvalue='?')))

	# generators producing Cartesian products lazily

	print(list(itertools.product('ABA', range(3), repeat=3)))
	print(list(itertools.combinations('ABA', 2)))

	print(list(itertools.combinations_with_replacement('ABA', 3)))

	print(list(itertools.islice(itertools.count(start=1, step=2), 3))) #because otw count goes indef

	#cy = itertools.cycle('Denisa') # next(cy) goes one letter at a time forever

	print(list(itertools.permutations('ABA', 2)))

	print(list(itertools.repeat(4, 2))) # can go on forever if number of repeats not given

	# rearrange items
	# tee gives multiple generators
	g1, g2 = itertools.tee('ABC', 2)
	print(next(g1)); print(next(g2))
	print(next(g2)); print(next(g1))

	# reversed needs a sequence but only provides one item at a time as needed
	print(list(reversed(range(5))))

	# the widely used groupby; this generator yields tuples of (key, group_generator)
	# input should be sorted or clustered
	print(list(itertools.groupby('Ddddennnniiiissaaa')))

	for letter, group_gen in itertools.groupby('Ddddennnniiiissaaa'):
		print(letter, len(list(group_gen)))


	fruits = ['apple', 'epple', 'pear', 'mear']
	# fruits.sort(key=len)

	for length, group in itertools.groupby(reversed(sorted(fruits, key=len)), len):
		print(length, list(group))


	#iterable reeducing
	# all and any better than reduce because theey short circuit eraly
	print(all([1, 2, 3]))
	print(any([True, False]))

	# remember min max with key like sorted
	print(min(['ABA', 'AB'], key=len))
	# print(max..)

	# notice sum with start like enumerate; start is added
	# print(sum([1, 2, 3], start = 2)) # this does not seem to work anymroe

	import functools
	print(functools.reduce(lambda x, y: x/y, [1, 2, 3], 8)) # 8 is an initial value
	# reduce applies to firs pair of elem; then result and next pair etc; 

	#-----------------------------------------
	# Ch 14: else close in for, while and try;
	# @contextmanager

	# EAFP style (easier to ask for forgiveness than permission) coding style in Python. 
	# Uses try except else code. In try block only test for the block intended. Put under else
	# after_class(). 
	# LBYL style is in C and Jaa look before you leap. Many if statements. Can lead to 
	# race condition between looking and leaping in multithreaded environemnts. (will need to know).

	# So what I have seen already - a way to avoic if clauses is tp use while, for /else
	# catch error if it happens.
	# typically there is a while/for with a break; else executes if while and for 
	# complete without the break comming into effect.
	# This seems to be very relevant.

	#Eg:
	my_list1 = ['apple', 'pear', 'banana']
	for item in my_list1:
		if item == 'banana': break
	else:
		raise ValueError('No banana flavor') # nothin is raised if banana is found an there is a break

	my_list = ['apple', 'pear']

	while item in my_list:
		if item == 'banana': break
	else:
		print('printing')

	try:
		assert 'banana' in my_list1 # my_list gives error
	except:
		raise ValueError
	else:
		print('else')


		# -------------
		# str
	import string
	s = 'Denisa'
	s.isalpha()
	s.isdecimal() # better
	s.isnumeric() # other types of numerals
	s.replace('i', 'f')
	s.endswith('a')
	s.upper()
	s.lower()
	s.strip()
	s.casefold()
	s.isidentifier() # valid var name: a-z, _, 0-9
	string.ascii_uppercase 
	string.printable # # to get printable ascii chars
	[chr(i) for i in range(128)] # to get ascii chars # inverse of ord(i) : Unicode code point of 8 bit string i
	s.count('.') # to count in string or list

	# -----------------------Counter 
	import collections
	s = 'aaabcaddd'
	c = collections.Counter(s)
	print(list(c.elements())) # with pos val
	t = 'abc'
	c1 = collections.Counter(t)
	print(c & c1) # common keys in min count

	print(c1 | c)
	print(c1 - c)
	print(c - c1) # usual set operations logic # pos values
	# counter(list or tuple or dict or string)
	c.most_common(2)
	c.update({'a':-7})
	print(c)
	print(c+c1) # a will result in neg val - disaap in c+c1

	# -------------------------------------Sorted Containers
	import sortedcontainers
	from sortedcontainers import SortedSet, SortedDict

	d = SortedDict(c)
	print(d)
	print(d.pop('a')) # val
	print(d) # w/o a
	print(d.popitem(-2)) # (c, 1) is the 2nd to last item
	print(d.get('a', 0))  # default is a not in
	print(d)

	# ------------------bisect
	import bisect
	# bisect.bisect(nums)
	# bisect.bisect_left(nums)
	# bisect.insort(nums)

	# aslo tuple
	a = [(1,2),(3, 4)]
	bisect.insort(a, (2, 5))
	print(a)
	a.insert(0, (6, 7)) # O(N)
	print(a)
	# ----------------sort 2 lists
	a = [ 1, 2, 3]
	b = [3, 2, 1]
	print(sorted(zip(b, a)))

	# tuples
	list(enumerate(a))

	#list comprehension with if else
	[x+1 if x >= 45 else x+5 for x in l]

	# list comprehensoin with if only
	[x+1 for x in l if x < 5]
 
	# list of lists comprehension

	[[] for _ in range(n)]

	# --------------
	d = {(1, 2, 3): 5}
	print(d[1, 2, 3]) # don't need to parans key tuple

	# to assign from tuple
	x, y = (1, 2)
	print(x, y)

	# -------------------
	# - Int can be encoded in 4 bytes.
	# - Char can be encoded in 1 byte.
	# ------------------

	# -------------------
	print(f"{5:b}") # print binary representation of number 5 = 101

	print(isinstance(c, int))

	a = -5 % 2
	b = 2 - 5 % 2 
	print(a, b) # nega mod k = k - posa mod k

	# ---------------
	a = [ 1, 2, 3]
	b = map(lambda x: x**2, a)
	print(list(b))

	print(list(filter(lambda x: x > 2, a))) # only 3



	# ----------
	set1 = {2, 3, 1}
	print(frozenset(set1))

	# ------------
	# - List of dicts is faster and more efficient than dict of lists
	# - Prefer comprehensions over map and filters and lambda functions (fluent python)

	# =======================
	import copy
	d1 = {'a':1, 'b':2}
	d2 = copy.deepcopy(d1)
	d3 = d1
	print(d2)
	print(id(d1), id(d2), id(d3))

	# ---------------
	import random
	# range(n, 0, -1): includes n but not 0
	random.randint(3, 5) # includes 3 and 5 O(1) op
	random.choice([1, 2, 3])
	print(random.randrange(1, 3)) # seemst that 3 is excluded

	random.random() [0, 1)

	# -----------------

	# - Can do list comprehension like this: starts = [i if x == T[0] else None for i,x in enumerate(S)]

	# - You can test true false condition like this: if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0
	# - You can assign like this: board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])

	# you can say root1 is root2 to test if 2 tree nodes are the same

	# --------------------------
	# how to get bytes in int in a string so that can be used in compression, for example
	# string chunks= len_to_str_via_bytes+chunk

	x = 26 # 0xff is 255
	bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
	bytes.reverse()
	bytes_str = ''.join(bytes_str)

	# then back to int
	res = 0
	for c in bytes_str:
		res = res * 256 + ord(c)

	# to get hostname in http://0.0.0.0/8080 
	 host = 'http://'+startUrl.split('/')[2]

	 
	 *arg are positional arguments
	 **kwargs are named arguments



	
if __name__ == '__main__':
	main()
