def triplets(d: [int], t: int):
    """
    Brute force: O(3)
    1. Sort d
    2. i start from 0, j from the next index that d[j] != d[i], k from next index that d[k] != d[j]
    3. keep moving k until sum >= t
    4. keep moving j until sum >= t
    """
    
    # n = len(d)

    # if n < 3:
    #     return 0

    # sorted_d = sorted(d)
    
    

    # i = 0


    # triplets = []

    # while i < n and sorted_d[i] <= t:
    #     if i > 0 and sorted_d[i] == sorted_d[i - 1]:
    #         i += 1
    #         continue
    #     j = i + 1
    #     while j < n and sorted_d[i] + sorted_d[j] <= t:    
    #         if sorted_d[j] == sorted_d[i] or sorted_d[j] == sorted_d[j - 1]:
    #             j += 1
    #             continue
    #         else:
    #             k = j + 1
    #             while k < n and sorted_d[i] + sorted_d[j] + sorted_d[k] <= t:
    #                 if sorted_d[k] == sorted_d[j] or sorted_d[k] == sorted_d[k - 1]:
    #                     k += 1
    #                     continue
    #                 else:
    #                     triplets += [[i, j, k]]
    #                     k += 1
    #             j += 1
    #     i += 1
    # return triplets

    """
    Optimized: O(2)
    1. Sort d
    2. i start from 0, j from next index that d[j] != d[i], k from n - 1
    3. k decrease until sum smaller than k, then add all solutions from j to k, and increase j 
    """


print(triplets([1,2,3,4,5], 8))



