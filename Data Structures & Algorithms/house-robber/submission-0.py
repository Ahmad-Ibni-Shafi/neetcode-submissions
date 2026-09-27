class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(idx,dp):
            if idx==0:
                return nums[0]
            if idx<0:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            pick = solve(idx-2, dp) + nums[idx] 
            notPick = solve(idx-1, dp)
            dp[idx] = max(pick, notPick)
            return dp[idx]
        n = len(nums)
        dp = [-1]*n
        return solve(len(nums)-1, dp)