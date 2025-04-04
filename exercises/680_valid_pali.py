
#On space O1
def validPalindrome(self, s: str) -> bool:
    def check(i,j,s):
        while i<j:
            if s[i] != s[j]:
                return False
            i +=1
            j-=1
        return True
    i,j = 0,len(s)-1
    while i<j:
        if s[i] != s[j]:
            return check(i+1,j,s) or check(i,j-1,s)
        i+=1
        j-=1
    return True

