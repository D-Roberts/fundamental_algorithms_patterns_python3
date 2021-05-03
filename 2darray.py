"""
2D

"""
import collections

# the 2 trades problem key trick
 # Find the Maximum money with 2 tradesfor i -> 0 to prices.length-1    max_2_trades = Max(max_2_trades, best_till_i[i] + best_from_i[i+1])

# transpose and reverse cols to rotate clockwise by 90

def transpose(a):
	for i in range(len(a)):
		for j in range(i, len(a)):
			a[i][j], a[j][i] = a[j][i], a[i][j]

def flip_rows(a):
	for i in range(len(a)):
		a[i][:] = a[i][::-1]

def zig_zag_print(a):
	m, n = len(a), len(a[0])
	r, c = 0, 0
	up = True
	while True:
		print(a[r][c])
		if r ==0 or r == m - 1:
			c += 1
			print(a[r][c])
			up = not up
		elif c == 0 or c == n - 1:
			r += 1
			print(a[r][c])
			up = not up
		if r == m - 1 and c == n - 1:
			break
		r = r - 1 if up else r + 1
		c = c + 1 if up else c - 1

# rotate array by x elem; revers; reverse first x; reverse last n - x.
def rotate_x(a, x):
	a.reverse()
	a[:x] = a[:x][::-1] # this should be last n-x
	a[x:] = a[x:][::-1] 

def reverse_words_in_sent(sent):
	a = list(sent)
	a.reverse()
	prev = 0
	n = len(a)
	for i in range(n - 1):
		if i+1 < n and a[i+1] == ' ' and prev < n:
			a[prev:i+1] = a[prev:i+1][::-1]
			prev = i + 2

			a[prev:] = a[prev][::-1]
	return  ' '.join(a)


def longest_palindromic_substring(s):
	"""O(nsq sol, not Mancher O(n))"""
	if not s: return 0 
	start, end = 0, 0
	ml, n = 1, len(s)

	def valid(i):
		return i >= 0 and i < n

	for i in range(n):
		off = 0
		while valid(i - 1- off) and valid(i + 1 +  off) and s[i - 1- off] == s[i + 1 + off]:
			off += 1
		lc = 2 * off + 1
		if lc > ml:
			ml = lc 
			start, end = i - off, i + off
			
	for i in range(n):
		off = 0
		while valid(i - off) and valid(i + 1 + off) and s[i - off] == s[i + 1 + off]:
			off += 1
		el = 2 * off 
		if el > ml:
			ml = el
			start, end = i - off + 1, i + off

	return ml, (start, end)
	

def multiply(self, num1: str, num2: str) -> str:
        if not num1 and not num2: return ""
        def _add(a, b):
            if a and not b: return a
            elif b and not a: return b
            elif not a and not b: return []
            carry, ares = 0, []
            smaller, larger = (b, a) if len(a) > len(b) else (a, b)
            while smaller:
                carry, partial = divmod(smaller.pop() + larger.pop() + carry, 10)
                ares.append(partial)
            while larger:
                carry, partial = divmod(larger.pop() + carry, 10)
                ares.append(partial)
            if carry:
                ares.append(carry)      
            return list(reversed(ares))
        
        smaller, larger = (num1, num2) if len(num1) < len(num2) else (num2, num1)
        res = []
        for i, a in enumerate(reversed(smaller)):
            carry, p = 0, [0] * i
            for j, b in enumerate(reversed(larger)):
                carry, cres = divmod(int(b) * int(a) + carry, 10)
                p.append(cres)
            if carry: p.append(carry)
            res = _add(res, list(reversed(p)))
        return "0" if all(x==0 for x in res) else "".join([str(x) for x in res])
        
def stock_profit_1trade(nums):
	min_so_far = ..
	max_diff = ..
	return max_diff # common approach to see min_so_far, max_so_far; sometimes from  both ends. Stock trade problems relevant.
	# TODO: 2 trades, and the variations.
	
def main():
	s = 'abacda'
	
	
if __name__ == '__main__':
	main()
