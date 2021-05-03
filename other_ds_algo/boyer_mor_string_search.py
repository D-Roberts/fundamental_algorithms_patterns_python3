# Boyer moore
"""
Search for pattern in string. Grep implements it.

Combines 2 heuristics:
1. Bad character heuristic
2. The good suffix heuristic

Code for 1 :O(mn) worst case where all same letter. O(n/m) best case
"""

def boyer_moor1(text, p):

    def get_bad_char(p, m):

        bad_char = [-1] * 256

        for i in range(m):
            bad_char[ord(p[i])] = i #last occ

        return bad_char


    s = 0 # shift
    n, m = len(text), len(p)
    bad_ch = get_bad_char(p, m)
    # print(bad_ch)

    i = 0

    while i <= n - m: # substring in teext starts at i
        s = 0

        for j in reversed(range(m)):
            if p[j] != text[i+j]:
                s = max(1, j - bad_ch[ord(text[i+j])]) # shift to the last occ in p of the mismatched char at i+j inn text
                break
        if s == 0:
            return i # found it
       
        i += s