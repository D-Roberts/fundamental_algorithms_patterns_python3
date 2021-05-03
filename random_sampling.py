# randoms

# Reservoir sampling
'''
Variations on:

-stream i = 1, ... k, ...n
- r= [0, 1, 2, ..k-1] indices

- maintain list of random samplee of size k.

- at i = k; len(r) = k; P(any j in 0..k-1) = 1/k

- if i = k + 1 : n = k+1 elem so far; each with 1/i = 1/(k+1) probab


Algo:
- to maintain: k -len random sample: where probab of each elem is k/n

j = random.randint(1, i)  # inclusive for when i is somewhere after k
if j < k: replace in reser

- Variation:
- build reservoir on the fly
- pick the new element; don't replace in reserv if need only 1 elem with prob 1/n; 

'''

def reserv(i, last_picked):
	'''
	from stream pick random numer; don;t know total n; know i so far
	[1, 2 .. i] 
	I want 1/n; last num is num i=k+1; 1/i from total i numbers; i/n
	'''
	k = i
	i = k + 1

	j = random.randint(1, i)

	if j <= k:
		return last_picked
	return j # do probab decision diagram: 1 to i with p = i/n and i+1 to n with p (n-i)/n; then from 1 to i; pick j; if j <=k : with p = k / i pick prev;
	# if k < j <= i : pick j (if i = k + 1 then p = 1/i) but this chunk has i/n probab so codni: is (i/n) * (1/i) = 1/n.

	
def reservoir_linked(ll):
	""" return random node with equal probab; without intermed storage; p = 1/n
	reservoir sampling where i < n, n unknown; so far k; current i = k + 1; pick current if rand = i if rand < i: the previous picked.
	"""
	curr = ll.head
	i = 1
	num = 0

	while curr:
		j = random.randint(1, i)
		if j == i:
			num = curr.val
		curr = curr.next
		i += 1

	return num

