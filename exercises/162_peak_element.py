

from typing import List

# Ologn space O1
def findPeakElement(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]) and (
            mid == 0 or nums[mid] > nums[mid - 1]
        ):
            return mid
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo  # unreachable

# variant: valley, find value that is smaller than neighboor

# Ologn space O1
def findPeakElement2(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]) and (
            mid == 0 or nums[mid] < nums[mid - 1]
        ):
            return mid
        if nums[mid] > nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo  # unreachable


print(findPeakElement2([1,2,3,1]))