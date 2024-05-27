from collections import deque
import copy;
def solution(n, wires):
    answer = 1e9
    def bfs(start,visited, graph):
        visited[start] = True;
        count = 0;
        queue = deque();
        queue.append(start);
        while queue:
            cur_node = queue.popleft();
            count += 1;
            for next_node in graph[cur_node]:
                if visited[next_node] == False:
                    visited[next_node] = True;
                    queue.append(next_node);
                    
        return count;
    for w in wires:
        temp = copy.deepcopy(wires);
        temp.remove(w);
        graph = [[] for _ in range(n+1)];
        visited = [False for _ in range(n+1)];
        results = [];
        for wire in temp:
            graph[wire[0]].append(wire[1]);
            graph[wire[1]].append(wire[0]);
        
        for i in range(1,n+1):
            if visited[i] == False:
                results.append(bfs(i,visited,graph));
        results.sort(reverse = True);
        answer = min(answer,results[0] - results[1]);
              
    return answer