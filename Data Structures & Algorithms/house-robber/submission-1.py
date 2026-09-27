class Solution:
    def rob(self, nums: List[int]) -> int:
    # Tabulation
        n = len(nums)
        dp = [-1]*n
        dp[0] = nums[0]
        for idx in range(1,n):
            if idx>1:
                pick = nums[idx] + dp[idx-2]
            else:
                pick = nums[idx]
            notPick = dp[idx-1]
            dp[idx] = max(pick, notPick)
        return dp[n-1]


    # Memoization:
        # def solve(idx,dp):
        #     if idx==0:
        #         return nums[0]
        #     if idx<0:
        #         return 0
        #     if dp[idx] != -1:
        #         return dp[idx]
        #     pick = solve(idx-2, dp) + nums[idx] 
        #     notPick = solve(idx-1, dp)
        #     dp[idx] = max(pick, notPick)
        #     return dp[idx]
        # n = len(nums)
        # dp = [-1]*n
        # return solve(len(nums)-1, dp)