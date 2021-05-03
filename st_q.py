"""
Stacks and queues.

"""
import collections

def find(s, N):
	if not s: return False
	found = False
	temp = []
	while s:
		if s[-1] == N:
			found = True
			break
		temp.append(s.pop())
	while temp:
		s.append(temp.pop())
	return Found 

class Q:
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enq(self, x):
		self.s1.append(x)

	def deq(self):
		if not self.s2:
			self.flush()
		if not self.s2:
			raise IndexError
		return self.s2.pop()

	def flush(self):
		while self.s1:
			self.s2.append(self.s1.pop())

class ArrayStack:
	def __init__(self, size):
		self.a = [0] * self.size
		self.s1 = 0
		self.s2 = size - 1
		assert int(size) == size and size is not None

	def push(self, s, x):
		assert s == 's1' or s == 's2'
		assert self.s1 <= self.s2 and self.s1 < len(self.a) and slef.s2 >= 0
		if s == 's1':
			self.a[self.s1] = x
			 self.s1 += 1
		else:
			self.a[self.s2] = x
			self.s2 -= 1
	def pop(self, s):
		if s == 's1' and self.s1 > 0:
			return self.a[self.s1 - 1]
		elif s == 's2' and self.s2 < len(self.a) - 1:
			return self.a[self.s2+1]
		else:
			raise IndexError

class Stack_Max:
	Elem_Max = collections.namedtuple('El_Max', ('element', 'max'))
	def __init__(self):
		self.stack = []
		
	def empty(self):
		if len(self.stack) == 0: return True
		return False

	def push(self, x):
		if self.empty():
			self.stack.append((x, x))
		self.stack.append((x, max(x, self.max())))

	def max(self):
		if self.empty():
			raise IndexError("max():empty stack")
		return self.stack[-1].max

	def pop(self):
		if self.empty():
			raise IndexError("pop():empty stack")
		return self.stack.pop().element

class Stack_Max:
	def __init__(self):
		self.s = []
		self.m = []

	def push(self, x):
		self.s.append(x)
		if not self.m or self.m[-1] < x:
			self.m.append(x)
		
	def get_max(self):
		try:
			maxv = self.m[-1]
			return maxv
		except:
			raise IndexError

	def pop(self):
		try:
			top = self.s.pop()
			if top == self.m[-1]:
				self.m.pop()
			return top
		except:
			raise IndexError("pop():empty q")


def eval_simple_expr(s):
	operators = ['+', '/', '-', '*']
	def precedence(op):
		if op in ['+', '/']: return 1
		return 2

	s_op, s_num = [], []
	def process(sop, snum):
		num1 = snum.pop()
		op = sop.pop()
		num2 = snum.pop()
		result = eval(num2 + op + num1)
		snum.append(result)

	if not s: return 0
	for ch in s:
		if ch not in operators:
			snum.append(ch)
		elif ch in operators:
			while s_op and precedence(s_op[-1] >= precedence(ch)):
				process(s_op, snum)
			s_op.append(ch)
	while s_op:
		process(s_op, snum)
	return snum.pop()

	"""
	# add parans
	
	for ch in s:
		if ch.isdigit():
			snum.append(ch)

		elif ch in ops:
			while ops and precedence(ops[-1]) >= precedence(ch):
				process(ops, snum)
			ops.append(ch)

		elif ch == '(':
			ops.append(ch)

		elif ch == ')':
			while ops and ops[-1] != '(':
				process()
			ops.pop()

	while ops:
		process()

	return snum.pop()
	"""


def FIFOQ:
	"""Can have LL or array implem"""
	def __init__(self, size):
		self.size = size
		self.a = [None] * size
		self.len = 0
		self.f = 0
		self.b = 0

	def add(self, x):
		assert self.len < self.size
		self.a[self.b] = x
		self.b = (self.b + 1) % self.size
		self.len += 1

	def remove(self):
		assert self.len > 0
		result = self.a[self.f]
		self.f = [self.f + 1] % self.size
		self.len -= 1
		return result

def slide_win_sum(nums, k=3):
	q = collections.dequeu()
	s = 0
	for el in nums:
		if len(q) == k:
			sel = q.popleft()
			s -= sel
		q.append(el)
		s += el 
		if len(q) == k:
			print(s)

class Q_Max:
	def __init__(self):
		self.q = collections.deque()
		self.m = collections.deque()

	def enq(self, x):
		self.q.appendleft(x)
		# add back pop front
		while self.m and self.m[0] < x:
			self.m.popleft()
		self.m.appendleft(x)

	def get_max(self):
		try:
			return self.m[-1]
		except:
			raise IndexError

	# use with sliding window
	# back() 3 2 1 (front)
	# max 3
	def deq(self):
		try:
			el = self.q.pop()
			if el == self.m[-1]:
				self.m.pop()
			return el
		except:
			IndexError("pop():empty q")


def main():
	s = 'abacda'
	
	
if __name__ == '__main__':
	main()
