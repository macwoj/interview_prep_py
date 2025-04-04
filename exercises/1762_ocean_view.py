
from typing import List

# On space On
def findBuildings(heights: List[int]) -> List[int]:
    result = []
    height = 0
    for i in range(len(heights)-1,-1,-1):
        if heights[i] > height:
            result.append(i)
        height = max(heights[i],height)
    result.reverse()
    return result

#variant: return number of buildings
# On space: O1
def findBuildings(heights: List[int]) -> List[int]:
    count=0
    height=0
    for i in range(len(heights)-1,-1,-1):
        if heights[i]>height:
            count+=1
            height=heights[i]
    return count

#variant:ocean on both sides
# On space On
# [2,5,3,10,9,8]
# out [0,1,3,4,5]
def findBuildings2(heights: List[int]) -> List[int]:
    if len(heights) == 1:
        return heights
    left = 0
    left_max = 0
    right_max = heights[-1]
    right = len(heights)-1
    left_view = [0]
    right_view = [len(heights)-1]
    while left < right:
        if heights[left] < heights[right]:
            left+=1
            if left < right and heights[left] > left_max:
                left_max = heights[left]
                left_view.append(left)
        else:
            right-=1
            if left < right and heights[right] > right_max:
                right_max = heights[right]
                right_view.append(right)
    return left_view+right_view[::-1]

print(findBuildings2([2,5,3,10,9,8])) # [0,1,3,4,5]