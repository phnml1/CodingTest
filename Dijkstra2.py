import heapq;
from collections import defaultdict;
#내풀이
def delaytime(times,n,k):
    graph = {};
    for time in times:
        if time[0] not in graph:
            graph[time[0]] = []
        graph[time[0]].append((time[2], time[1]))
    costs = {}
    pq = []
    heapq.heappush(pq,(0,k));
    while pq:
        cur_cost, cur_v = heapq.heappop(pq);
        if cur_v not in costs:
            costs[cur_v] = cur_cost;
            if len(costs) == n:
                return cur_cost;
            if cur_v in graph:
                for cost,next_v in graph[cur_v]:
                    next_cost = cur_cost + cost;
                    heapq.heappush(pq,(next_cost, next_v));
    return -1;
            
#강의 풀이
def delaytime2(times,n,k):
    graph = defaultdict(list);
    for time in times:
        graph[time[0]].append((time[2],time[1]));
    costs = {}
    pq =[]
    heapq.heappush(pq,(0,k));
    while pq:
        cur_cost, cur_node = heapq.heappop(pq);
        if cur_node not in costs:
            costs[cur_node] = cur_cost;
            for cost,next_node in graph[cur_node]:
                next_cost = cur_cost + cost;
                heapq.heappush(pq,(next_cost, next_node));
    for node in range(1,n+1):
        if node not in costs:
            return -1;
    return (max(costs.values()));
graph = [[1,2,1]];
print(delaytime(graph,2,1));