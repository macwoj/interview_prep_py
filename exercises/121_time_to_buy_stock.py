
from typing import List


def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    max_profit = 0
    min_price = prices[0]
    for p in prices:
        min_price = min(min_price,p)
        max_profit = max(max_profit,p-min_price)
    return max_profit

# variant: min cost of departures and returns, buy dept then buy return in future
# On
def minCost(departures,returns):
    if not departures or not returns or len(returns) < 2 or len(departures) != len(returns):
        return -1
    dep_cost = departures[0]
    ret_cost = returns[1]  ## HERE, need to be in the future
    result = dep_cost+ret_cost
    for i in range(2,len(departures)):
        ret_cost=min(ret_cost,returns[i])
        result=min(result,dep_cost+ret_cost)
        dep_cost = min(dep_cost,departures[i])
    return result


print(minCost([1,2,3,4],[4,3,2,1])) # 2