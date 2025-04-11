
# On space O1
def isNumber(s: str) -> bool:
    if not s:
        return False
    i = 0
    period = False
    exponent = False
    digit = False
    edigit = False
    while i < len(s):
        if s[i] in {'+','-'}:
            if i > 0 and s[i-1] not in {'e','E'}:
                return False
        elif s[i] == '.':
            if period or exponent:
                return False
            period = True
        elif s[i] in {'e','E'}:
            if not digit or exponent or i == len(s) - 1:
                return False
            exponent = True
        elif not s[i].isdigit():
            return False
        else:
            digit = True
            if exponent:
                edigit = True
        i += 1
    if exponent and not edigit:
        return False
    return digit

#variant: no exp
def isNumber2(s: str) -> bool:
    if not s:
        return False
    i = 0
    period = False
    digit = False
    while i < len(s):
        if s[i] in {'+','-'}:
            if i > 0:
                return False
        elif s[i] == '.':
            if period:
                return False
            period = True
        elif not s[i].isdigit():
            return False
        else:
            digit = True
        i += 1
    return digit