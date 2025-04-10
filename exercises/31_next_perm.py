
# On space: O1
from typing import List

def nextPermutation(self, nums: List[int]) -> None:
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

#variant: prev permutation
# On space: O1
def nextPermutation2(self, nums: List[int]) -> None:
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