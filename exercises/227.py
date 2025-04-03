
# Leetcode 227
def caculator(s):
    prev = 0
    curr = 0
    result = 0
    op = '+'
    for i in range(len(s)):
        c = s[i]
        if c.isdigit():
            curr = curr*10 + int(c)
        if (c != ' ' and not c.isdigit()) or i == len(s)-1:
            if op =='+':
                result += prev
                prev = curr
            elif op=='-':
                result += prev
                prev = -curr
            elif op=='*':
                prev = prev*curr
            elif op=='/':
                prev=prev/curr
            curr=0
            op = c
    return result + prev

# variant no - and /
def caculator2(s):
    prev = 0
    curr = 0
    result = 0
    op = '+'
    for i in range(len(s)):
        c = s[i]
        if c.isdigit():
            curr = curr*10 + int(c)
        if (c != ' ' and not c.isdigit()) or i == len(s)-1:
            if op =='+':
                result += prev
                prev = curr
            elif op=='*':
                prev = prev*curr
            curr=0
            op = c
    return result + prev

print(caculator('3+3'))
print(caculator('3+3*3*3'))