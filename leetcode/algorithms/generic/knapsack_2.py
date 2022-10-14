def knapsack_recur(profit: [int], weight: [int], i: int, capacity: int):
    if i < 0 or i >= len(profit) or capacity < 0:
        return 0
    
    profit_1 = 0
    if weight[i] <= capacity:
        profit_1 = profit[i] + knapsack_recur(profit, weight, i + 1, capacity - weight[i])

    return max(profit_1, knapsack_recur(profit, weight, i + 1, capacity))
