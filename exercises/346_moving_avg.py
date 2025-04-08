
class MovingAverage:

    def __init__(self, size: int):
        self.sum = 0
        self.size = size
        self.q = deque()

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.size:
            self.sum -= self.q.popleft()
        return float(self.sum) / float(len(self.q))
    
#variant: int division, return list of results
# On, space O1
def movingAvg(nums,k):
    res = 0
    result = []
    for i,v in enumerate(nums):
        res+=v
        if i>=k:
            res-=nums[i-k]
        if i>=k-1:
            result.append(res//k)
    return result
        
print(movingAvg([5,2,8,14,3],3)) # 5,8,8