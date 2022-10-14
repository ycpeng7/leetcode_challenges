# -*- coding: utf-8 -*-
"""
Given a list of objects, values, and weights. Find the maximum value that could fit in a bag with the weight limit.

@author: joepa
"""

def knapsack_recur(value, weight, W: int):
    n = len(value)
    # Find max of 2 possible siutations:
    # 1. nth item included with the remaining weight composing of n-1 items
    # 2. nth item not included, max value of n-1 items
    if n == 0 or W == 0:
        return 0
    if weight[n-1] > W:
        return knapsack_recur(value[:n-1], weight[:n-1], W)
    else:
        return max(
            knapsack_recur(value[:n-1],
                           weight[:n-1],
                           W - weight[n-1]) + value[n-1],
            knapsack_recur(value[:n-1],
                           weight[:n-1],
                           W)
                  )


def knapsack_memo(value, weight, W: int, memo):
    n = len(value)
    if n == 0 or W == 0:
        return 0
    if not memo[n]:
        if weight[n-1] > W:
            memo[n-1] = knapsack_memo(value[:n-1], weight[:n-1], W, memo)
        else:
            memo[n] = max(
                    knapsack_memo(value[:n-1],
                                   weight[:n-1],
                                   W - weight[n-1], memo) + value[n-1],
                    knapsack_memo(value[:n-1],
                                   weight[:n-1],
                                   W, memo)
                  )
    return memo[n]


def knapsack_bottomup(value, weight, W: int):
    n = len(value)
    memo = [[None for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                memo[i][w] = 0
            else:
                if weight[i-1] > W:
                    memo[i][w] = memo[i-1][w]
                else:
                    memo[i][w] = max(memo[i-1][w-weight[i-1]] + value[i-1],
                                     memo[i-1][w])
    return memo[n][W]





print(knapsack_recur([60, 100, 120], [10, 20, 30], 50))
print(knapsack_memo([60, 100, 120], [10, 20, 30], 50, [0, None, None, None]))
print(knapsack_bottomup([60, 100, 120], [10, 20, 30], 50))
