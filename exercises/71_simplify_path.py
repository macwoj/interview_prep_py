
def simplifyPath(path: str) -> str:
    sta = []
    tok = path.split('/')
    for t in tok:
        if not t:
            continue
        elif t == '.':
            continue
        elif t =='..':
            if sta:
                sta.pop()
        else:
            sta.append(t)

    return '/'+'/'.join(sta)

#variant: given cwd and cd, cd is the change, return the path that applies cd to cwd
# cwd = '/a/b/c' cd =/d/./e out='/d/e'
def simplifyPath2(cwd,cd) -> str:
    if not cd:
        return cwd
    if cd[0] =='/':  ##HERE
        cwd=''
    sta = cwd.split('/')[1:]
    toks = cd.split('/')
    for tok in toks:
        if not tok:
            continue
        elif tok=='.':
            continue
        elif tok=='..':
            if sta:
                sta.pop()
        else:
            sta.append(tok)
    return '/'+'/'.join(sta)

print(simplifyPath('/home/user/Documents/../Pictures'))

print(simplifyPath2('/a/b/c','/d/./e'))
print(simplifyPath2('','/d/./e'))
print(simplifyPath2('/a/b/c',''))
print(simplifyPath2('/a/b','.//c/../../d/f'))