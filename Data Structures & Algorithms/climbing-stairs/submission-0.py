class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(n,dp):
            if n<=1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = solve(n-1, dp) + solve(n-2, dp)
            return dp[n]
        dp = [-1]*(n+1)
        return solve(n,dp)