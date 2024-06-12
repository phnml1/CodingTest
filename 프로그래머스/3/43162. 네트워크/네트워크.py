from collections import deque,defaultdict

def solution(n, computers):
    answer = 0
    graph = defaultdict(list);
    visited = [0 for _ in range(n)];
    def bfs(x):
        queue = deque();
        queue.append(x);
        while queue:
            cur = queue.popleft();
            for a in graph[cur]:
                if visited[a] == 0:
                    visited[a] = 1;
                    queue.append(a);
        return 1;
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i!=j:
                graph[i].append(j);
        
    for i in range(n):
        if visited[i] == 0:
            answer += bfs(i);
    
    return answer