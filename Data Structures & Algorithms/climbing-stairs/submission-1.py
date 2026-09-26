class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        # def solve(n,dp):
        #     if n<=1:
        #         return 1
        #     if dp[n] != -1:
        #         return dp[n]
        #     dp[n] = solve(n-1, dp) + solve(n-2, dp)
        #     return dp[n]
        # dp = [-1]*(n+1)
        # return solve(n,dp)