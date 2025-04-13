
from collections import defaultdict
from typing import List


class Solution:
    def shift(self,str):
        res = []
        amount = ord(str[0]) - ord('a')
        for c in str:
            res.append(chr((ord(c)-amount)%26))
        return ''.join(res)
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for s in strings:
            shift = self.shift(s)
            lookup[shift].append(s)
        return [lookup[k] for k in lookup]
    
#variant: rotational cipher, right shift , a wraps to z, A to Z, 9 to 0, others stay the same
class Solution2:
    def rotate(self,s,factor):
        result=[]
        if factor==0:
            return s
        for c in s:
            if c.islower():
                tmp = ord(c)+factor-ord('a')
                tmp = tmp%26+ord('a')
                result.append(chr(tmp))
            elif c.isupper():
                tmp = ord(c)+factor-ord('A')
                tmp = tmp%26+ord('A')
                result.append(chr(tmp))
            elif c.isdigit():
                tmp = ord(c)+factor-ord('0')
                tmp = tmp%10+ord('0')
                result.append(chr(tmp))
            else:
                result.append(c)
        return ''.join(result)

s=Solution2()
assert s.rotate("minMerz-894",5) == "rnsRjwe-349"
assert s.rotate("XYZ_abo_112288",39) == "KLM_nob_001177"