class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(nums,i):
            if i>=len(nums):
                ans.append(subset[:])
                return
            
            subset.append(nums[i])
            solve(nums, i+1)
            subset.pop()
            solve(nums, i+1)
            
        ans = []
        subset = []
        solve(nums,0)
        return ans
        