
# O(max(n,m)) space O1
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j = len(num1)-1,len(num2)-1
        rem = 0
        result = []
        while i>=0 or j>=0:
            res = rem
            if i>=0:
                res += ord(num1[i])-ord('0')
                i-=1
            if j>=0:
                res += ord(num2[j])-ord('0')
                j-=1
            result.append(chr(res%10+ord('0')))
            rem = res//10
        if rem:
            result.append(chr(rem+ord('0')))
        result.reverse()
        return ''.join(result)
    
#variant: there are decimals
# O(max(n,m)) space O1
class Solution2:
    def addString(self,num1,num2,rem=0):
        i,j = len(num1)-1,len(num2)-1
        result = []
        while i>=0 or j>=0:
            res = rem
            if i>=0:
                res += ord(num1[i])-ord('0')
                i-=1
            if j>=0:
                res += ord(num2[j])-ord('0')
                j-=1
            result.append(chr(res%10+ord('0')))
            rem = res//10
        return result,rem
    
    def addStrings(self, num1: str, num2: str) -> str:
        tok1 = num1.split('.')
        tok2 = num2.split('.')
        dec1 = tok1[1] if len(tok1) == 2 else ''
        dec2 = tok2[1] if len(tok2) == 2 else ''
        max_l = max(len(dec1),len(dec2))
        dec1 = dec1.ljust(max_l,'0')
        dec2 = dec2.ljust(max_l,'0')
        result,rem = self.addString(dec1,dec2)
        if result:
            result.append('.')
        res,rem = self.addString(tok1[0],tok2[0],rem)
        result.extend(res)
        if rem:
            result.append(chr(rem+ord('0')))
        result.reverse()
        print(result)
        return ''.join(result)
    
s=Solution2()
assert s.addStrings('111','111') == '222'
assert s.addStrings('111.1','111.1') == '222.2'
assert s.addStrings('111.1234','111.1') == '222.2234'
assert s.addStrings('.1234','1.1000000') == '1.2234000'
assert s.addStrings('.1234','1.') == '1.1234'
assert s.addStrings('.9234','.1') == '1.0234'