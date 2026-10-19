class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def solve(i):
            if i<=len(candidates) and sum(sub)==target: 
                if sub not in ans:
                    ans.append(sub[:])
                return
            if sum(sub)>target or i>=len(candidates):
                return 
            for j in range(i,len(candidates)):
                if j>i and candidates[i]==candidates[i-1]:
                    continue
                sub.append(candidates[j])
                solve(j+1)
                sub.pop()

        ans = []
        sub = []
        solve(0)
        return ans

