import heapq;
def solution(maps):
    n,m = len(maps),len(maps[0]);
    d = [(1,0),(0,1),(-1,0),(0,-1)];
    queue = [];
    queue.append((1,0,0));
    visited = [[1e9 for _ in range(m)] for _ in range(n)];
    while queue:
        cost,x,y = heapq.heappop(queue);
        for i in range(4):
            dx,dy = d[i];
            next_cost,next_x,next_y = cost+1,x+dx,y+dy;
            if 0<=next_x<n and 0<=next_y<m:
                if maps[next_x][next_y] == 1 and next_cost < visited[next_x][next_y]:
                    heapq.heappush(queue,(next_cost,next_x,next_y));
                    visited[next_x][next_y] = next_cost;
    if visited[n-1][m-1] == 1e9:
        return -1;
    return visited[n-1][m-1];