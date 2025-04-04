
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = len(nums1) - 1
    n -= 1
    m -= 1
    while i >= 0:
        if n >= 0 and m >= 0:
            if nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
        elif m >= 0:
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1
        i -= 1

#variant: not given n and m

def merge2(nums1: List[int], nums2: List[int]) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = len(nums1)-1
    n = len(nums2)-1
    m = len(nums1)-len(nums2)-1
    while i >= 0:
        if n >= 0 and m >= 0:
            if nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
        elif m >= 0:
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1
        i -= 1
    return nums1

print(merge2([1,8,0,0],[3,5]))