
# On space: O1
from typing import List

# find first decreasing element i, swap with first greater from right, reverse i+1
def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    valley=-1
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            valley=i
            break
    if valley==-1:
        nums.reverse()
        return
    next=len(nums)-1
    while nums[next]<=nums[valley]:
        next-=1
    nums[next],nums[valley]=nums[valley],nums[next]

    left = valley+1
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums

#variant: prev permutation
# On space: O1
def nextPermutation2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    peak=-1
    for i in range(len(nums)-2,-1,-1):
        if nums[i] > nums[i+1]:
            peak=i
            break
    if peak==-1:
        nums.reverse()
        return
    next=len(nums)-1
    while nums[next]>=nums[peak]:
        next-=1
    nums[next],nums[peak]=nums[peak],nums[next]

    left = peak+1
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums

print(nextPermutation([9, 4, 8, 3, 5, 5, 4, 3]))
print(nextPermutation2([9, 4, 8, 3, 5, 5, 6, 6]))