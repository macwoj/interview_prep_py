
class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        for c in s:
            if result and c==result[-1]:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)
    
#variant: return string removing all dups
# On space:On
class Solution2:
    def removeDuplicates(self, s: str) -> str:
        result = []
        i=0
        while i<len(s):
            c=s[i]
            if not result:
                result.append([c,1])
            elif c==result[-1][0]:
                result[-1][1]+=1
            elif result[-1][1]>1:
                result.pop()
                continue
            else:
                result.append([c,1])
            i+=1
        if result[-1][1]>1: ### HERE
            result.pop()
        return ''.join([x[0] for x in result])

s = Solution2()
assert s.removeDuplicates('abbbacxss') == 'cx'