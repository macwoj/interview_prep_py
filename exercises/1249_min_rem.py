
from collections import defaultdict


def minRemoveToMakeValid(s: str) -> str:
    balance=0
    total=0
    tmp=[]
    for c in s:
        if c==')':
            if balance>0:
                tmp.append(c)
                balance-=1
        elif c=='(':
            balance+=1
            total+=1
            tmp.append(c)
        else:
            tmp.append(c)
    result=[]
    keep = total-balance
    for c in tmp:
        if c=='(':
            if keep >0:
                keep-=1
                result.append(c)
        else:
            result.append(c)
    return ''.join(result)

#variant: inplace
def minRemoveToMakeValid2(s: str) -> str:
    s=list(s)
    balance=0
    total=0
    j = 0
    for i,c in enumerate(s):
        if c==')':
            if balance>0:
                s[j] = s[i]
                j+=1
                balance-=1
        elif c=='(':
            balance+=1
            total+=1
            s[j] = s[i]
            j+=1
        else:
            s[j] = s[i]
            j+=1
    s = s[:j]
    keep = total-balance
    j=0
    for i,c in enumerate(s):
        if c=='(':
            if keep >0:
                keep-=1
                s[j] = s[i]
                j+=1
        else:
            s[j] = s[i]
            j+=1
    return ''.join(s[:j])

# more braces () [] {}
def minRemoveToMakeValid3(s: str) -> str:
    s=list(s)
    balance = defaultdict(int)
    total = defaultdict(int)
    closing = {
        ')':'(',']':'[','}':'{'
    }
    j = 0
    for i,c in enumerate(s):
        if c.isalnum():
            s[j]=s[i]
            j+=1
        else:
            if c in closing:
                if balance[closing[c]] > 0:
                    s[j]=s[i]
                    j+=1
                    balance[closing[c]]-=1
            else:
                s[j]=s[i]
                j+=1
                balance[c]+=1
                total[c]+=1
    s=s[:j]
    keep = defaultdict(int)
    for k in total:
        keep[k] = total[k]-balance[k]
    j=0
    for i,c in enumerate(s):
        if c.isalnum():
            s[j]=s[i]
            j+=1
        else:
            if c in closing:
                s[j]=s[i]
                j+=1
            else:
                if keep[c]>0:
                    s[j]=s[i]
                    j+=1
                    keep[c]-=1
    return ''.join(s[:j])

print(minRemoveToMakeValid("lee(t(c)o)de)"))
print(minRemoveToMakeValid2("lee(t(c)o)de)"))

print(minRemoveToMakeValid3(")[]]{{}"))