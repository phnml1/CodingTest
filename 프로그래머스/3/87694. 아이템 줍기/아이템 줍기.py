from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[-1 for _ in range(102)] for _ in range(102)];
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x: x*2, r);
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    board[i][j] = 0;
                elif board[i][j] != 0:
                    board[i][j] = 1;
    queue=deque();
    queue.append((characterX*2, characterY*2));
    visited = [[1 for _ in range(102)] for _ in range(102)];
    while queue:
        x,y = queue.popleft();
        if x == itemX*2 and y == itemY*2:
            return visited[x][y]//2
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i];
            if 0<=next_x<102 and 0<=next_y<102:
                if board[next_x][next_y] == 1 and visited[next_x][next_y] == 1:
                    queue.append((next_x,next_y));
                    visited[next_x][next_y] = visited[x][y] + 1;
