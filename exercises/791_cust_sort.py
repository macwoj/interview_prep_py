
from collections import defaultdict

# O(S+26+26) = Os space: O26
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        result = []
        for c in order:
            if c in freq:
                result.extend([c]*freq[c])
                del freq[c]
        for c in freq:
            result.extend([c]*freq[c])
        return ''.join(result)
    
#variant: order param is vector of chars
# same implementation
class Solution2:
    def customSortString(self, order: str, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        result = []
        for c in order:
            if c in freq:
                result.extend([c]*freq[c])
                del freq[c]
        for c in freq:
            result.extend([c]*freq[c])
        return ''.join(result)
    
#variant: optimize further? store using list
# O(S+26+26) = Os space: O26
class Solution3:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0]*26
        for c in s:
            freq[ord(c)-ord('a')] += 1
        result = []
        for c in order:
            val = ord(c)-ord('a')
            if freq[val] > 0:
                result.extend([c]*freq[val])
                freq[val] = 0
        for i,c in enumerate(freq):
            if c>0:
                result.extend([chr(i+ord('a'))]*c)  #HERE
        return ''.join(result)
    
s=Solution3();
assert s.customSortString('cba','abcd') == 'cbad'