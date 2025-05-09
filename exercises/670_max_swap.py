
#On*O10
# 
def maximumSwap(self, num: int) -> int:
    num_str = list(str(num))
    right = [0]*10
    for i,v in enumerate(num_str):
        right[ord(v)-ord('0')]=i #find all postions of numbers, rightmost will win
    for i in range(len(num_str)):
        n = ord(num_str[i])-ord('0')
        # go from 9 to the number and see if its postion is on right, if so swap and return
        for j in range(9,n,-1): # we dont need to check n since we only care about bigger
            if right[j] > i:
                num_str[i],num_str[right[j]]=num_str[right[j]],num_str[i]
                return int(''.join(num_str))
    return num

# variant: input int array, return second biggest number
# 3*On = On storage O10 = O1
def secondMax(nums):
    if not nums or len(nums)<2:
        return []
    freq = [0]*10
    for n in nums:
        freq[n]+=1
    result = []
    for i in range(9,-1,-1): #construct biggest umber by using highest number and creating using frequency
        if freq[i] > 0:
            result.extend([i]*freq[i])
    for i in range(len(result)-1,0,-1): #swap first number from right
        if result[i]!=result[i-1]:
            result[i],result[i-1]=result[i-1],result[i]
            return result
    return []

    

print(secondMax([2,7,3,6])) #7 6 2 3
print(secondMax([1,2,1,1,1])) # 1 2 1 1 1