from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[-1 for _ in range(102)] for _ in range(102)];
    dir = [(1,0),(0,1),(-1,0),(0,-1)];
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x: x*2,r);
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    board[i][j] = 0;
                elif board[i][j] != 0:
                    board[i][j] = 1;
                    print((i,j));
    visited = [[0 for _ in range(102)] for _ in range(102)];
    queue = deque();
    queue.append((characterX*2,characterY*2));
    visited[characterX*2][characterY*2] = 1;
    while queue:
        x,y = queue.popleft();
        for dx,dy in dir:
            nx,ny = x+dx,y+dy;
            if 0<=nx<102 and 0<=ny<102:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx,ny));
                    visited[nx][ny] = visited[x][y] + 1;
    return visited[itemX*2][itemY*2]//2 