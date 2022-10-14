class WaysToSum: 

    def ways_recur(i, total):
        if self.memo[i-1] is not None:
            return self.memo[i-1]
        else:
            memo[i-1] = 1 + ways_recur(i, total - 1)


    def ways(total, k):
        total_ways = 0
        self.memo = [None] * k
        for i in range(1, k + 1):
            total_ways += ways_recur(i, k)