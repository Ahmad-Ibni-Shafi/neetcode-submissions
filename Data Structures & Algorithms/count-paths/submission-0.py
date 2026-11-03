class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Memoization
        dp = [[-1]*n for _ in range(m)]
        def func(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up = func(i-1,j)
            left = func(i,j-1)
            dp[i][j] = up+left
            return dp[i][j]

        return func(m-1,n-1)