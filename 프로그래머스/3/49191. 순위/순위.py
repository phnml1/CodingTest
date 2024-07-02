from collections import defaultdict, deque;

def bfs(win_nodes, lose_nodes,a,visited):
    queue = deque();
    queue.append(a);
    while queue:
        node = queue.popleft();
        for i in win_nodes[node]:
            if visited[i] == False:
                queue.append(i);
                visited[i] = True;
    queue.append(a);
    while queue:
        node = queue.popleft();
        for i in lose_nodes[node]:
            if visited[i] == False:
                queue.append(i);
                visited[i] = True;
    return visited.count(True);
def solution(n, results):
    answer = 0
    win_nodes = defaultdict(list);
    lose_nodes = defaultdict(list);    
    for result in results:
        a,b = result;
        lose_nodes[b].append(a);
        win_nodes[a].append(b);
    for i in range(1,n+1):
        visited = [False for _ in range(n+1)];
        if bfs(win_nodes, lose_nodes,i,visited) == n-1:
            answer += 1;
    return answer