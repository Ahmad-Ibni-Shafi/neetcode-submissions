class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l,r,s):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def solve(i):
            if i>=len(s):
                ans.append(part[:])
                return
            for j in range(i,len(s)):
                if isPalindrome(i,j,s):
                    part.append(s[i:j+1])
                    solve(j+1)
                    part.pop()

        part = []
        ans = []
        solve(0)
        return ans