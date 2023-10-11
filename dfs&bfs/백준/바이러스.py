from collections import deque;
# 내풀이
# num = int(input())
# pairnum = int(input())
# pairs = {}
# result = 0
# visited = {}
# for _ in range(pairnum):
#     n,m = map(int,input().split())
#     if n not in pairs:
#         pairs[n] = [m];
#     else:
#         pairs[n].append(m);
#     if m not in pairs:
#         pairs[m] = [n];
#     else:
#         pairs[m].append(n);
# queue = deque();
# queue.append(1);
# visited[1] = True;
# while queue:
#     cur_node = queue.popleft();
#     if cur_node in pairs:
#         for node in pairs[cur_node]:
#             if node not in visited:
#                 queue.append(node);
#                 visited[node] = True;
#                 result+=1;
# print(result);

n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
#BFS
# visited[1]=1
# queue = deque([1]);
# while queue: 
#     c = queue.popleft();
#     for nx in graph[c]:
#         if visited[nx] ==0:
#             queue.append(nx)
#             visited[nx]=1
# print(sum(visited)-1);
#DFS
def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] ==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1);
    