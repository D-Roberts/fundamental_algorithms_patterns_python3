"""
LinkedLs.

Also remember the dummy head trick.

"""
class Node:
	def __init__(self, x):
		self.x = x
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = self.head

	def traverse(self, n):
		i, curr = 0, self.head
		while i < n-1:
			if curr != None:
				curr = curr.next
			else:
				print("list is shoerte")
		if curr == None: print('shorter')
		return curr

# Sort linked list
class Node:
	def __init__(self, x):
		self.x = x
		self.next = None

class LL:
	def __init__(self):
		self.head = None
		self.tail = self.head

	def append(self, node):
		if self.head is None:
			self.head = node 
		else:
			self.tail.next = node
		self.tail = node

def append_list(result, listi):
	if listi is None or listi.head is None:
		return

	result.append(listi.head)
	result.tail = listi.tail

def sort_ll(input):
	list0, list1, list2 = LL(), LL(), LL()
	curr = input.head
	if curr == None: return Nones
	while curr is not None:
		if curr.x == 0: list0.append(curr)
		elif curr.x == 1: list1.append(curr)
		else list2.append(Curr)
		curr = curr.next 

	result = LL()
	appen_list(result, list0)
	appen_list(reult, list1)
	appen_list(result, list2)
	return result 

def odd_evens(ll):
	if ll is None or ll.head is None:
		return (None, None)
	lo, le = LL(), LL()
	curr, i = ll.head, 0

	while curr is not None:
		if i % 2:
			lo.append_list(curr)
		else:
			le.append_list(curr)
		curr = curr.next 
		i += 1

	if lo.tail is not None: lo.tail.next = None
	if le.tail is not None: le.tail.next = None
	return (lo, le)

# delete node when prev given
def del_node_after(ll, n):
	if n == LL.tail:
		return
	next = n.next; n.x = next.x
	delete(LL, next, n)

# slow fast get cycle
def has_cycle(LL):
	if LL is None or LL.head is None:
		return False

	fast, slow = LL.head, LL.head

	while fast is not None:
		fast = fast.next
		if slow == fast:
			return True
		if fast is not None:
			fast = fast.next
			if fast == slow: return True
		slow = slow.next 

	return False


def get_cycle_len(LL):
	fast, slow = head, head
	while fast is not None:
		fast = fast.next 
		if fast == slow:
			break
		if fast is not None:
			fast = fast.next
			if fast == slow:
				break
		slow = slow.next
	if fast is None: return -1
	fast = fast.next 
	c = 1
	while fast != slow:
		fast = fast.next
		c += 1
	return c

def get_median(LL):
	fast, slow = head, head 
	while fast it not None and fast.next is not None: # not sure this is correct actually for even length of LL
		fast = fast.next.next
		slow = slow.next
	return slow

# LRU Cache implem with DLL and dict; find an ordered dict implem
class LRU:
	def __init__(self, capacity):
		self.c = capacity
		self.d = collections.defaultdict(Node)
		self.ll = LL()
		self.head = self.ll.head
		self.tail = self.ll.tail

	def read(self, key):
		node = self.d[key]
		if node is None:
			return

		self._remove(key)
		self._add(nod.key, node.val)

		return node.val

	def write(self, key, val):
		if not self.c:
			self._remove(self.head.key)
			self.c += 1
		node = Node(key, val)
		self._add(key, val):
		self.c -= 1

	def _remove(self, key):

		if key not in self.d.keys():
			return
		node = self.d[key]
		self._remove_from_LL(node)
		del self.d[key]

# now ll helpers; LL has prev node (DLL)
	def _remove_from_LL(self, node):
		if node.prev != None:
			node.prev.next = node.next

		if node.next is not None:
			node.next.prev = node.prev

		if node is self.head:
			self.head = node.next

		if nose is self.tail:
			self.tail = node.prev
	def _add_to_ll(self, node):
		if self.head is None:
			self.head = node
		else:
			self.tail.next = node
			node.prev = tail

		tail = node

class Node:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None
		self.prev = None

class LL:
	def __init__(self):
		self.head = None
		self.tail = None

# reverse ll in place

def reverse(ll.head):
	prev, curr = None, head
	while curr is not None:
		next = curr.next
		curr.next = prev
		prev = current
		current = next

	return prev 

# ll is palin; reverse part of list
def is_palin(head):
	if head is None:
		return False
	fast, slow = head, head 

	while fast is not None and fast.next is not None and fast.next.next is not None:
		fast = fast.next.next
		slow = slow.next 
	median = slow
	current = median.next
	prev = median
	# rev after median
	while curr is not None:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next 

	front, back = head, prev # this may or may not be correct; should use helpers for median and for reversed
	while back is not None and front is not None and front != back:
		if front.x != back.x:
			return False
			front, back = front.next, back.next
	return True

def main():
	s = 'abacda'
	
	
if __name__ == '__main__':
	main()
