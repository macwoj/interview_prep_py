from collections import Counter
import random





def findTarget(s,target):
    result=[]
    def dfs(s,i,solution,solSum,target):
        nonlocal result
        if i==len(s):
            if target == solSum:
                tmp = []
                for i,v in enumerate(solution):
                    if v>=0 and i>0:
                        tmp.append('+'+str(v))
                    else:
                        tmp.append(str(v))
                result.append(''.join(tmp))
                return
            else:
                return
        solution.append(int(s[i]))
        dfs(s,i+1,solution,solSum+solution[-1],target)
        solution.pop()
        solution.append(-int(s[i]))
        dfs(s,i+1,solution,solSum+solution[-1],target)
        solution.pop()
        if i>0:
            prev = solution.pop()
            solution.append(int(str(prev)+s[i]))
            dfs(s,i+1,solution,solSum-prev+solution[-1],target)
            solution.pop()
            solution.append(prev)
    dfs(s,0,[],0,target)
    for r in result:
        print(f'{r} {eval(r)}')
    return result


# print(findTarget('123',4))
# print(findTarget('12345',10))
# print(findTarget('12345',15))
print(findTarget('12345',12345))
print([findTarget('123456789',10)])