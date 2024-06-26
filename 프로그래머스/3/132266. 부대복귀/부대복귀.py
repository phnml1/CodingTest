from collections import deque
from collections import defaultdict
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)];
    for road in roads:
        s,e = road[0],road[1];
        graph[s].append(e);
        graph[e].append(s);

    queue = deque();
    costs = defaultdict(lambda:-1);
    queue.append((0,destination));
    costs[destination] = 0;
    while queue:
        cost, node = queue.popleft();
        for i in graph[node]:
            if costs[i] == -1:
                costs[i] = cost+1;
                queue.append((cost+1,i));
                if i == destination:
                    break;
    return [costs[source] for source in sources]