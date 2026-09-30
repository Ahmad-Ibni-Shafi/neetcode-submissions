class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def solve(cost):
            n = len(cost)
            dp = [-1]*(n+1)
            dp[0] = 0
            dp[1] = 0
            for i in range(2,n+1):
                dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
            return dp[n]
        return solve(cost)



            # if i>= len(cost):
            #     return 0
            # if dp[i]!= -1:
            #     return dp[i]
            # take_1step = solve(i+1, cost,dp)
            # take2_step = solve(i+2, cost,dp)
            # dp[i] = cost[i]+ min(take_1step, take2_step)
            # return dp[i]

        # n = len(cost)
        # dp = [-1]*n
        # step0 = solve(0,cost,dp)
        # step1 = solve(1,cost,dp)
        # return min(step0, step1)