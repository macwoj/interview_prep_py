
# On
def isPalindrome(self, s: str) -> bool:
    i,j=0,len(s)-1
    while i<j:
        while i<j and not s[i].isalnum():
            i+=1
        while i<j and not s[j].isalnum():
            j-=1
        if s[i].lower()!=s[j].lower():
            return False
        i+=1
        j-=1
    return True

# variant: only inlcude chars in include vector
def isPalindrome2(s,include):
    chars = set(include)
    i,j=0,len(s)-1
    while i<j:
        while i<j and s[i] not in chars:
            i+=1
        while i<j and s[j] not in chars:
            j-=1
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


print(isPalindrome2('racecarX',['r','X'])) # False
print(isPalindrome2('Yo, banana boY',['Y','o','b','a','n'])) # True