"""
# Rank Transform of an Array

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their
  rank must be the same.
- Rank should be as small as possible.

 

## Example 1:

- Input: `arr = [40,10,20,30]`
- Output: `[4,1,2,3]`
- Explanation: 40 is the largest element. 10 is the smallest. 20 is the second
  smallest. 30 is the third smallest.

## Example 2:

- Input: `arr = [100,100,100]`
- Output: `[1,1,1]`
- Explanation: Same elements share the same rank.

## Example 3:

- Input: `arr = [100,200,100,200]`
- Output: `[1,2,1,2]`

 

Constraints:

```
0 <= arr.length <= 105
-109 <= arr[i] <= 109
```

Leetcode 1331
"""

"""
1. Sort the input list from smallest to largest
2. Create dict with value as key, index + 1 (rank) as value of the dict, if key already exist, don't do any thing
3. Map the input value to the dictionary to get the rank
"""

def rank_transform(input: [int]):
    sorted_list = sorted(input)
    rank_dic = {}
    rank = 1
    for item in sorted_list:
        if rank_dic.get(item) is None:
            rank_dic[item] = rank
        rank += 1
    return [rank_dic[item] for item in input]

assert rank_transform([40,10,20,30]) == [4,1,2,3]
assert rank_transform([100,100,100]) == [1,1,1]
assert rank_transform([100,200,100,200]) == [1,3,1,3]
assert rank_transform([]) == []


