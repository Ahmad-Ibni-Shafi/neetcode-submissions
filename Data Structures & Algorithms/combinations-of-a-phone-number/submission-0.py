class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'}
        def solve(i):
            if i>=len(digits):
                ans.append(''.join(sub[:]))
                return 
            for ch in dic[digits[i]]:
                sub.append(ch)
                solve(i+1)
                sub.pop()
                
        sub=[]
        ans=[]
        if len(digits)==0:
            return []
        solve(0)
        return ans