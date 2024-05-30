def solution(n, costs):
    answer = 0;
    costs.sort(key = lambda x: x[2]);
    parent = [0 for _ in range(n)];
    
    def find_parent(a):
        if parent[a] != a:
            parent[a] = find_parent(parent[a]);
        return parent[a];
    
    def union_parent(a,b):
        a = find_parent(a);
        b = find_parent(b);
        if a<b:
            parent[b] = a;
        else:
            parent[a] = b; 
    for i in range(n):
        parent[i] = i;
    for cost in costs:
        if find_parent(cost[0]) != find_parent(cost[1]):
            union_parent(cost[0],cost[1]);
            answer += cost[2]
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))