class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def solve(idx,sub):
            if sum(sub)==target:
                if sub not in ans:
                    ans.append(sub[:])
            if idx>=len(nums) or sum(sub)>target:
                return 

            sub.append(nums[idx])
            solve(idx, sub)
            sub.pop()
            solve(idx+1, sub)
   
        ans = []
        solve(0,[])
        return ans
        
        