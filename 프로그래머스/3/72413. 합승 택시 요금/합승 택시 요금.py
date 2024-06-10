from collections import defaultdict
import heapq
def solution(n, s, a, b, fares):
    answer = 0
    graph = defaultdict(list);
    for fare in fares:
        start,end,c = fare
        graph[end].append((c,start));
        graph[start].append((c,end));
    def dijkstra(a):
        costs = [1e9] * (n+1);
        costs[a] = 0;
        queue = [];
        heapq.heappush(queue,(0,a));
        while queue:
            cost,node = heapq.heappop(queue);
            if costs[node]<cost:
                continue;
            for next_cost,next_node in graph[node]:
                if next_cost + cost <costs[next_node]:
                    costs[next_node] = next_cost + cost
                    heapq.heappush(queue,(next_cost+cost,next_node));
        return costs
    
    D = [0] + [dijkstra(i) for i in range(1, n+1)] 
    path = 1e9
    for i in range(1, n+1):
        path = min(path, D[s][i] + D[i][a] + D[i][b])
    return path