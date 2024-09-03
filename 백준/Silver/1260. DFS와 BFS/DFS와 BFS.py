import sys;
from collections import deque;
input = sys.stdin.readline;

n,m,v = map(int,input().split());
graph = [[] for _ in range(n+1)];

def bfs(start,graph):
    visited = [];
    queue = deque();
    queue.append(start);
    visited.append(start);
    while queue:
        cur = queue.popleft();
        for node in sorted(graph[cur]):
            if node not in visited:
                visited.append(node);
                queue.append(node);
    return visited;

def dfs(start,graph,visited):
    visited.append(start);
    if len(visited) == len(graph)-1:
        return;
    for i in sorted(graph[start]):
        if i not in visited:
            dfs(i,graph,visited);
            

for _ in range(m):
    a,b = map(int,input().split());
    graph[a].append(b);
    graph[b].append(a);
df = []
bf = bfs(v,graph);
dfs(v,graph,df);
for value in df:
    print(value, end = ' ');
print();
for value in bf:
    print(value, end = ' ');