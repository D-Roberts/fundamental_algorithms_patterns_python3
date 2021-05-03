"""
HAsh tables

"""
import collections

def rabin_karp(s, t):
	'''larger S contains target T. Find index where'''
	x = 53
	hasht, hashs = 0, 0 
	for i in range(len(t)):
		hasht = hasht * x + t[i]
		hashs = hashs * x + s[i]

	if hasht == hashs and t == s[0:len(t)]:
		return 0 # found at index 0

	xpow = 1

	for i in range(len(t), len(s)):
		to_remove = s[i - len(t)]
		hashs = (hashs - to_remove * xpow) * x + s[i]
		if hash == hasht and s[i-len(t)+1:i+1] == t: return i - len(t) + 1
	return -1

# Stream of char P 1032 wi trie
class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.trie = {}
        self.dq = collections.deque([])
        
        for word in set(words):
            node = self.trie 
            for ch in word[::-1]: #trie from reversed
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word


    def query(self, letter: str) -> bool:
        self.dq.appendleft(letter)
        node = self.trie
        for ch in self.dq:
            if '$' in node: return True
            if ch not in node: return False
            node = node[ch]
        return '$' in node
        

def main():
	s = 'abacda'
	
	
if __name__ == '__main__':
	main()
