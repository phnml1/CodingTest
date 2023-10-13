from collections import deque

c,r = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(r)];
dic = {}
visited = [[False] * c for _ in range(r)]
result = 9999;
for i in range(r):
    for j in range(c):
        if arr[i][j] in dic:
            dic[arr[i][j]].append((i,j));
        else:
            dic[arr[i][j]] = [(i,j)];
        
d = [(0,1),(1,0),(0,-1),(-1,0)];
def bfs(ripedic):
    q = deque()
    for ripe in ripedic:
        riper,ripec = ripe
        visited[riper][ripec] = True
        q.append((riper, ripec, 0))  # 0으로 초기화된 일수를 큐에 추가
    while q:
        riper, ripec, ripeday = q.popleft()
        for a in range(4):
            dr, dc = d[a]
            cur_r = riper + dr
            cur_c = ripec + dc

            if 0 <= cur_r < r and 0 <= cur_c < c and not visited[cur_r][cur_c]:
                if arr[cur_r][cur_c] == 0:
                    q.append((cur_r, cur_c, ripeday + 1))  # 일수 업데이트
                    visited[cur_r][cur_c] = True
    return ripeday  # 마지막에 도달한 과일까지의 최소 일수 반환

if 1 in dic:
    result = bfs(dic[1])
else:
    result = 0  
for i in range(r):
        for j in range(c):
            if arr[i][j] ==0 and visited[i][j]==False:
                result = -1
                break;
print(result);

