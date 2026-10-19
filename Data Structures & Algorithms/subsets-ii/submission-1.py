class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def solve(i):
            if i==len(nums):
                if sub not in ans:
                    ans.append(sub[:])
                return      
            if i>=len(nums):
                return
            sub.append(nums[i])
            solve(i+1)
            sub.pop()
            solve(i+1)
        sub = []
        ans = []
        solve(0)
        return ans
