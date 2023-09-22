
from collections import deque


def NumIsLands(grid):
    number_of_islands= 0
    #행
    m = len(grid)
    #열
    n = len(grid[0])
    visited = [[False]*n for _ in range(m) ]
    
    def bfs(x,y):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        visited[x][y] = True
        queue = deque()
        queue.append((x,y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                #지도넘어서는지
                if next_x>=0 and next_x<m and next_y>=0 and next_y<n:
                    #섬이고 방문을했었는지
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
    for i in range(m):
        for j in range(n):
            #땅이면서 & 방문 안했을때
            if grid[i][j]=="1" and not visited[i][j]:
                bfs(i,j)
                
                #dfs()
    return number_of_islands


NumIsLands(grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
])