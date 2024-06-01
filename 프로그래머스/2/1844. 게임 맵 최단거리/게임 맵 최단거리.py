from collections import deque;
def solution(maps):
    n,m = len(maps),len(maps[0]);
    d = [(1,0),(0,1),(-1,0),(0,-1)];
    queue = deque();
    queue.append((1,0,0));
    while queue:
        cost,x,y = queue.popleft();
        for i in range(4):
            dx,dy = d[i];
            next_cost,next_x,next_y = cost+1,x+dx,y+dy;
            if 0<=next_x<n and 0<=next_y<m:
                if maps[next_x][next_y] == 1:
                    maps[next_x][next_y] = next_cost;
                    if next_x == n-1 and next_y == m-1:
                        return next_cost;
                    queue.append((next_cost,next_x,next_y));
    return -1;