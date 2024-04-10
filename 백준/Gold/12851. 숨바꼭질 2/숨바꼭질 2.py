from sys import stdin
input = stdin.readline
from collections import deque

# 수빈 위치, 동생 위치
N, K = map(int,input().split())

MAX_SIZE = 100001

que = deque()
que.append(N)
visited = [-1]*MAX_SIZE
visited[N] = 0
cnt = 0

while que:
    # 현 위치
    current = que.popleft()
    # 도착
    if current == K:
        cnt += 1
    # 이동
    for next in [current*2,current+1,current-1]:
        # 범위 내
        if 0 <= next < MAX_SIZE:
            # 첫방문 혹은 방문 시간이 같은 경우가 이미 있음(가장 빠른 시간 방법의 수를 위해)
            if visited[next] == -1 or visited[next] >= visited[current] + 1:
                visited[next] = visited[current] + 1
                que.append(next)
 
print(visited[K])
print(cnt)