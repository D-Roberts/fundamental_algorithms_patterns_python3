"""
Trees

"""

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

def inorder_iterative_one(root):
	visited = set()
	
	if root is None:
		return root
	stack = []
	stack.append(root)
	while stack:
		node = stack.pop()
		if node in visited:
			print(node.val)
		else:
			if node.right:
				stack.append(node.right)
			stack.append(node)
			visited.append(node)
			if node.left:
				stack.append(node.left)

def inorder_iterative_two(root):
	'''O(logn) space'''
	stack = []
	node = root
	while node or stack:
		if node:
			stack.append(node)
			node = node.left
		else:
			node = stack.pop()
			print(node.val)
			node = node.right

def top_down_height(root):
	'''top down'''
	def _height(root, prev_height):
		if root is None:
			return
		curr_height = 1 + prev_height
		self.height = max(self.height, curr_height)
		_height(root.left, curr_height)
		_height(root.right, curr_height)

	_height(root, -1)
	return self.height

def print_all_paths_root_leaf(root):
	'''top dpwn'''
	
	def _path(root, path):
		if not root:
			return
		path.append(root)
		if is_leaf(root):
			print(path)
		_path(root.left)
		_path(root.right)
		path.pop()

	_path(root, [])

# bottom up
def get_heigh(root):
	if root is None:
		return -1
	return max(get_height(root.left), get_height(root.right)) + 1

# returns -1 if not balanced or hegith + 1
def get_balanced_w_height(root):
	if root is None:
		return 0
	lhs, rhs = get_balanced_w_height(root.left), get_balanced_w_height(root.right)
	if lhs == -1 or rhs == -1 or abs(lhs - rhs) > 1: return -1
	return max(lhs, rhs) + 1

def diameterOfBinaryTree(self, root): # not sure of this
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

def lca(node, p, q):
	if node is None:
		return None
	if node is p or node is q:
		return node
	lhs = LCA(node.left, p, q)
	rhs = LCA(node.right, p, q)
	if lhs is not None and rhs is not None:
		return node 
	return lhs if lhs is not None else rhs

#O(n)O(h)



def main():
	s = 'abacda'
	
	
if __name__ == '__main__':
	main()
