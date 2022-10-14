class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Ways to climb n stairs is
        way to climb n-1 stairs + way to climb n-2 stairs
        """
        
        ## Recursion
        
        # if n <= 2:
        #     return n
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        ## memoization
        
#         self.memo = [-1] * (n + 1)
        
#         def climbstairs_dp(n):
#             if n <= 2:
#                 return n

#             if self.memo[n] == -1:
#                 self.memo[n] = climbstairs_dp(n-2) + climbstairs_dp(n-1)

#             return self.memo[n]
        
#         return climbstairs_dp(n)
        
        ## bottom up
        
        if n <= 2:
            return n
        
        memo = [0] * (n + 1)
        memo[0], memo[1], memo[2] = 0, 1, 2
        

        for i in range(3, n + 1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]
    