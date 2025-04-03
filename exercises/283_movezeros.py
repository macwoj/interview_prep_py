
# Leetcode 283
def moveZeros(arr):
    s = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[s] = arr[s],arr[i]
            s+=1
    return arr

# variant: move zeros to front
def moveZeros2(arr):
    s = len(arr)-1
    for i in range(len(arr)-1,-1,-1):
        if arr[i] != 0:
            arr[i],arr[s] = arr[s],arr[i]
            s-=1
    return arr


print(moveZeros([0,1,3,0,4,5,0]))
print(moveZeros2([0,1,3,0,4,5,0]))
