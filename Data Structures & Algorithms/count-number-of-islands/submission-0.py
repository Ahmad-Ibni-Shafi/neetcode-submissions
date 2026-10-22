class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            r = len(grid)
            c = len(grid[0])
            queue = deque()
            queue.append((i,j))
            vis[i][j] = 1
            while len(queue)!=0:
                x,y = queue.popleft()
                for xx,yy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    new_i,new_j = x+xx, y+yy
                    if new_i<0 or new_i>=r or new_j<0 or new_j>=c or vis[new_i][new_j]==1 or grid[new_i][new_j]=='0':
                        continue
                    vis[new_i][new_j] = 1
                    queue.append((new_i, new_j))
                    

        r = len(grid)
        c = len(grid[0])
        vis = [[0 for _ in range(c)] for _ in range(r)]
        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1' and vis[i][j]==0:
                    count=count+1
                    bfs(i,j)
        return count