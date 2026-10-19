class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(i,op,cl):
            if i==n*2:
                if sub not in ans:
                    ans.append(''.join(sub[:]))
                return
            
            if op<n:
                sub.append('(')
                solve(i+1,op+1,cl)
                sub.pop()
            if op>cl:
                sub.append(')')
                solve(i+1,op,cl+1)
                sub.pop()
        sub=[]
        ans=[]
        solve(0,0,0)
        return ans