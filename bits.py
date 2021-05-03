"""
bits

"""


def set_bit(i, num, val):
	if val == 1:
		return (1 << i) | num
	return (~(1 << i)) & num 

def get_bit(num, i):
	return (num >> i) & 1

def swap_bits(num, i, j):
	if get_bit(num, i) != get_bit(num, j):
		return num ^ ((1 << i) | (1 << j))
	return num 

def reverse_bit_num(num, i, j):
	i, j = 0, 31
	while i < j:
		swap_bits(num, i, j)
		i += 1
		j -= 1

# set LSB to 0 x & (x - 1)
# x ^ x; 0 ^ x = x

def count_bits(num):
	count =0
	while (num):
		count += 1
		num = num & (num - 1)
	return count

def complement(num):
	# has all bits flipped starting with and after MSB (first 1 on the left)
	if num == 0:
		return 0
	MSB = math.log(2, num)
	return num^((1 <<(MSB+1) - 1))

def find_unique(a):
	mask = 0
	for n in a:
		mask ^= n
	return mask

def find_missing(n, a):
	mask = 1
	for i in range(1, n):
		mask ^= i

	for num in a:
		mask ^= num 
	return num #?? likely return mask

def main():
	s = 'abacda'
	x = 5

	# x & (x-1) sets LSB to 0; x & !(x-1) sets all except lsb to 0
	# int n has O(log(n)) set bits
	# every int = sum(of power of 2)
	print(x ^ 0 == x)
	print(x ^ 1 == 4) #should be not x but ~x is something else
	print(~x) # this is -6
	print(~(x - 1)) # this should be 2's complet here -5 ??
	print(x^x == 0, x & 0 == 0, x & 1 == x, x & x == x, x | 0 == x, x | 1 == 1, x | x == x)
	print('MSB', (x & ( x - 1)))
	print('lsb', x ^ (x&(x-1)))
	import math
	n = math.ceil(math.log(5))
	print(2**(n-1) - x) # is this 2 complem? is that a neg num?
	
if __name__ == '__main__':
	main()
