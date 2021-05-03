"""
BST

"""
import collections

# clean code that returns a list of nodes
def inorder(root):
	return inorder(root.left) + [root.val]  + inorder(root.right) if root else []
	
def valid_bst(root, low=float('-inf'), high=float('inf')):
	if root is None:
		return True
	return valid_bst(root.right, max(low, root.val), high)
	and valid_bst(root.left, low, min(high, root.val) and low < root.val < high


# del in O(H) 3 subcases
def find_first(root, target):
	'''occurence of target'''
	current = root
	result = None
	while current is not None:
		if current.val > target:
			current = current.left
		elif current.val < target:
			current = current.right
		else:
			result = current
			current = current.left
	return result

def successor(node, root):
	if node.right is not None:
		current = node.right
		while current.left is not None:
			current = current.left
		return current
	current = root
	successor = None
	while current is not None:
		if current.val > node.val:
			successor = current
			current = current.left
		elif current.val < node.val:
			current = current.right 
		elif current == node: break
	return successor 


def bst_lca(root, p, q):
    current = root 
    while current is not None:
        if current.val < p.val and current.val < q.val: current = current.right
        elif current.val > p.val and current.val > q.val: current = current.left 
        else: return current 
    return None # allow for not found

# balanced from linked list 
def get_median(head, tail):
    '''O(nlogn)'''

    fast, slow, prev_slow = head, head, None
    if head is None or tail is None:
        return None
    while fast is not None and fast != tail:
        fast = fast.next 
        if fast is not None and fast != tail:
            fast = fast.next
            prev_slow = slow
            slow = slow.next 
    return (slow, prev_slow)

def get_tree(head, tail):
    if head is None or tail is None:
        return None 
    med, prev = get_median(head, tail)
    # print(med.val)
    # print(prev.val)
    root = TreeNode(med.val)
    root.left = get_tree(head, prev)
    root.right = get_tree(med.next, tail)
    return root



class BST:
    def __init__(self, root):
        self.root = root

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if node.val < key:
            return self.search(node.right, key)
       return self.search(node.left, key)

    def _insert(self, key, root):
        if root is None:
            root = Node(key)
            return root
        else:
            if key == root.val:
                return root
            elif key < root.val:
                root.left = self._insert(key, root.left)
            else:
                root.right = self._insert(key, root.right)
        return root

    # def successor(self, node):
    #     current = self.root
    #     if node.right:
    #         current = node.right
    #         while current.left:
    #             current = current.left
    #         return current
    #     current = self.root
    #     successor = None

    #     while current:
    #         if current.val < node.val:
    #             current = current.right
    #         elif current.val > node.val:
    #             successor = current
    #             current = current.left
    #         elif current == node:
    #             break
    #     return successor


    # def delete(self, root, key):
    #     # cases: leaf; one child; 2 child: successor

    #     if root is None: return root

    #     if key < root.val:
    #         root.left = self.delete(root.left, key)
    #     elif key > root.val:
    #         root.right = self.delete(root.right, key)
    #     else: # this is the node to delete
    #         # leaf or no left 
    #         if root.left is None:
    #             temp = root.right
    #             root = None
    #             return temp
    #         elif root.right is None:
    #             temp = root.left
    #             root = None
    #             return temp
    #         else: # 2 childredn
    #             temp = self.succesor(root)
    #             root.key = temp.key
    #             root = self.delete(root, temp.val) # not clear how to do this ; need to start from root to delete

    def successor_right(self, node):

        # assume node.right exists
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def predecesor_left(self, node):
        # assume node left exists
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def delete(self, root, key):
        # use the simpler successor and predecessor cases for the 2 child cases
        if root is None:
            return None

        if key < root.val:
            root.left = self.delete(root.left)
        elif key > root.val:
            root.right = self.delete(root.right)

        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = self.predecesor_left(root)
        
                root.left = self.delete(root.left, root.val)
            elif root.right:
                root.val = self.successor_right(root)
                root.right = self.delete(root.right, root.val)
        return root

"""Self balancing trees for h = logn. 4 cases based on relationship of x - y - z
"""

class AVL:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 0

	def insert(self, root, key):

		# bst like insert
		if not root:
			return AVL(key)
		if key < root.val:
			return self.insert(root.left, key)
		return self.insert(root.right, key)

		# Step 2: geet the balance factor
		root.height = 1 + max(self.get_heigh(root.left), self.get_height(root.right))

		# get balance facotr
		bal_fact = self.get_balance(root) # left - right

		# Case 1: left left
		if key < root.left.val and bal_fact > 1:
			return self.rotate_right(root)

		# case 2: right right
		if key > root.right.val and bal_fact < -1:
			return self.rotate_left(root)

		# Case 3: Left Right: insert on the right branch of root.left y
		if key > root.left.val and balance > 1:
			root.left = self.rotate_left(root.left)
			return self.rotate_right(root)

		# case 4: right left: insert on left branch of root.right
		if key < root.right.val and balance > -1:
			root.right = self.rotate_right(root.right)
			return self.rotate_left(root)

		return root

	def rotate_left(self, z):
		y = z.right
		temp = y.left 
		y.left = z
		z.right = temp

		# update height
		y.height = 1 + max(self.get_height(y.left), self.get_heigh(y.right))
		z.heigh = 1 + max(self.get_height(z.left), self.get_height(z.right))

		return y

	def rotate_right(self, z):
		y = z.left
		temp = y.right
		y.right = z
		z.left = temp 

		# update height
		return y


"""Randomized BST"""

def Treap:


def main():
	s = 'must have a tree class'
	
	
if __name__ == '__main__':
	main()
