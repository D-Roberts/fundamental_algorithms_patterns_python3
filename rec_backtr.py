"""
Recursion and backtracking

"""
import collections

def pow(x, N):

	if x == 0 and N <= 0: 
		raise ValueError
	if x == 0:
		return 0

	def positive_pow(x, N):
		if N == 0: return 0
		if N == 1: return x
		res = positive_pow(x, N // 2)
		if N % 2 == 0:
			res = res * res
		if N % 2:
			res = res * res * x
		return res 

	res = positive_pow(abs(x), abs(N))

	if N < 0:
		res = 1/res 
	if x < 0 and n % 2:
		res = - res 
	return res 



  
# top down recursion
# print comb of k w buffer 

# Good python code that works for combinations of size k from  numbers 1 to n
def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backt(ind = 1, buff = []):
            if len(buff) == k:
                print(buff)
                res.append(buff[:])
                return
            
            # if ind > n:
                # return # no need for this in this case
            
            for i in range(ind, n+1):
                buff.append(i)
                backt(i+1, buff)
                buff.pop()
            
        res = []
        backt()
        return res
                
# Good python code for the power set (all subsets); thee knuth algo has a bitmaks sol all num i from 2**n to 2**(n+1)
# The power set generation is N *2**N
def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        
        def backt(ind, buff):
            res.append(buff[:])
            if len(buff) == n:
                return
            
            for i in range(ind, n):
                backt(i+1, buff + [nums[i]])
        
        
        res = []
        backt(0, [])
        return res


def print_combo(a, k):
	if not a or not k or k >= len(a): return

	def print_combos(a, k, buffer, buf_ind, arr_ind):
		if buf_ind == k:
			print(buffer)
			return
		if arr_ind == len(a):
			return 
		for i in range(arr_ind, len(a)):
			buffer[buf_ind] = a[i]
			print_combos(a, k, buf_ind+1, i+1)

	print_combos(a, k, [0] * k, 0, 0)

def word_from_phone_num_top_down_rec_buffer(num):
	# d = [mapping from nums to lettters on the phone]

	def top_down_buf(a, buff, ind):
		if len(buff) == len(a) or ind == len(a):
			print(buf)
			return

		letters = d[ind]
		if not letters:
			top_down_buf(a, buf, ind+1)
		for letter in letters:
			buff.append(letta)
			top_down_buf(a, buf, ind+1)
			buff.pop()
	top_down_buf(num, [], 0)

def all_subsets(a, buff, a_ind):
	print(buff)

	if len(buff) == len(a) or a_ind == len(a):
		return 

	for i in range(a_ind, len(a)):
		buff.append(i)
		all_subsets(a, buff, i + 1)
		buff.pop()

# good python code for permutations of len x generation (default to size of array)
 def permute(self, nums: List[int]) -> List[List[int]]:     
        # top down rec
        def perm_gen(i=0, x=len(nums), buff=[], is_in_set=set()):
            if len(buff) == x:
                # print(buff)
                ret.append(buff[:])
                # return 

            for i in range(len(nums)):
                if i not in is_in_set:
                    buff.append(nums[i])
                    is_in_set.add(i)
                    perm_gen(i, x, buff, is_in_set)
                    buff.pop()
                    is_in_set.discard(i)
        ret = []         
        perm_gen()
        return ret

def coinc_change(sum, coins, change, target, coin_Ind):
	if sum == target:
	print(change) # this is a list of coins
	return

	if sum > target:
		return

	for i in range(coin_Ind, len(coins)):
		change.append(coins[i])
		coinc_change(sum+coins[i], coins, change, target, i) # you can reuse coin00000
		change.pop()

# backtracking battleship
# 1. Core idea
# 2. Split in steps
# 3. Collect res from further call
# 4. Memoize
# 5. Base Case: wall ,out of bound, end of path etc.

def maze_path(a):
	d = collections.defaultdict(int)
	def oob(i, j):
		if i < 0 or j < 0 or i >= len(a) or j >= len(a[0]): return True
		return False

	def backtr(a, d, i ,j):
		if oob(i. j) or a[i][j] == 1:
			return False
		if d[i][j] in 1, 2:
			return False
		if i == len(a) - 1 and j == len(a[0]) - 1:
			return True

		d[(i, j)] = 1
		directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
		return any([backtr(a, d, s1, s2) for (s1, s2) in directions])
		d[(i, j)] = 2
		return False

	return backtr(a, d, 0, 0)




def sudoku(board): # tested
	boxes = [collections.defaultdict(int) for _ in range(9)] # list of dicts
	cols = [collections.defaultdict(int) for _ in range(9)]
	rows = [collections.defaultdict(int) for _ in range(9)]


	def box_id(r, c):
	    return (r//3) * 3 + c // 3

	for i in range(9):
	    for j in range(9):
	        if board[i][j] != '.':
	            cols[j][int(board[i][j])] = 1
	            rows[i][int(board[i][j])] = 1
	            boxes[box_id(i, j)][int(board[i][j])] = 1

	def place(r, c, cand):
	    boxes[box_id(r, c)][cand] += 1
	    rows[r][cand] += 1
	    cols[c][cand] += 1
	    board[r][c] = str(cand)

	def remove(r, c, cand):
	    boxes[box_id(r, c)][cand] = 0
	    rows[r][cand] = 0
	    cols[c][cand] = 0
	    board[r][c] = '.'

	def can_place(r, c, cand):
	    return not boxes[box_id(r, c)][cand] and not rows[r][cand] and not cols[c][cand]

	def next_pair(r , c):
	    if c == 8: return r+1, 0
	    return r, c+1

	def solve(r=0, c=0):
	    if r == 9:
	        return True
	    
	    nextr, nextc = next_pair(r, c)
	    if board[r][c] != '.': return solve(nextr, nextc)

	    for cand in range(1, 10):
	        if can_place(r, c, cand):
	            place(r, c, cand)
	            if solve(nextr, nextc): return True
	            remove(r, c, cand)
	    return False
	        
	solve()



def main():
	s = 'abacda'
	print(all_subsets(s, [], 0))
	
	
	
if __name__ == '__main__':
	main()
