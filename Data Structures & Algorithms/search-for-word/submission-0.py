class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(i,j,idx):
            if i<0 or i>=m or j>=n or j<0 or vis[i][j]==1 or board[i][j]!=word[idx]:
                return False
            if idx==len(word)-1:
                return True
            vis[i][j]=1
            if solve(i+1,j,idx+1):
                return True
            if solve(i-1,j,idx+1):
                return True
            if solve(i,j+1,idx+1):
                return True
            if solve(i,j-1,idx+1):
                return True
            vis[i][j]=0
            return False

        m = len(board)
        n = len(board[0])
        vis = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if solve(i,j,0):
                        return True
        return False

