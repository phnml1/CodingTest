from collections import deque;
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)];
    visited = [0 for _ in range(n+1)];
    for e in edge:
        graph[e[0]].append(e[1]);
        graph[e[1]].append(e[0]);
    queue = deque();
    queue.append(1);
    visited[1] = 1;
    while queue:
        cur = queue.popleft();
        for node in graph[cur]:
            if visited[node] == 0:
                visited[node] = visited[cur] + 1;
                queue.append(node);
    return visited.count(max(visited));