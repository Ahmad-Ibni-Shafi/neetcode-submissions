class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def solve(nums,i,sub,ans):
            if i==len(nums):
                if sub not in ans:
                    ans.append(sub[:])
                return    
             
            if i>=len(nums):
                return
            
            sub.append(nums[i])
            solve(nums, i+1,sub,ans)
            sub.pop()
            solve(nums, i+1,sub,ans)
        sub = []
        ans = []
        solve(nums,0,sub,ans)
        return ans