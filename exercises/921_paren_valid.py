
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        result = 0
        for c in s:
            if c=='(':
                balance+=1
            elif c==')':
                if balance==0:
                    result+=1
                else:
                    balance-=1
        result += balance
        return result
    
#variant: unlikely to get asked, return the actual string
class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        result = []
        for c in s:
            if c=='(':
                balance+=1
                result.append(c)
            elif c==')':
                if balance==0:
                    result.append('(')
                else:
                    balance-=1
                result.append(c)
            else:
                result.append(c)
        result.extend([')']*balance)
        return ''.join(result)

s=Solution2()
assert s.minAddToMakeValid('()))') == '()()()'
assert s.minAddToMakeValid('(()))((') == '(())()(())'