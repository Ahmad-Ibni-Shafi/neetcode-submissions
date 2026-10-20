class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        vis = [False]*n
        def solve(i):
            if i==n:
                res.append(sub[:])
                return
            for val in range(n):
                if vis[val]==True:
                    continue
                sub.append(nums[val])
                vis[val] = True
                solve(i+1)
                sub.pop()
                vis[val] = False
        sub=[]
        res=[]
        solve(0)
        return res



