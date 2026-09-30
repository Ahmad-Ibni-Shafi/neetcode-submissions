class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def solve(i,cost,dp):
            if i>= len(cost):
                return 0
            if dp[i]!= -1:
                return dp[i]
            take_1step = solve(i+1, cost,dp)
            take2_step = solve(i+2, cost,dp)
            dp[i] = cost[i]+ min(take_1step, take2_step)
            return dp[i]

        n = len(cost)
        dp = [-1]*n
        step0 = solve(0,cost,dp)
        step1 = solve(1,cost,dp)
        return min(step0, step1)