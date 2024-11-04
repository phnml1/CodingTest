from collections import Counter;

def move(graph, points, route):
    time = 0
    for i in range(len(route)-1):
        startr,startc,endr,endc = points[route[i]-1][0],points[route[i]-1][1],points[route[i+1]-1][0],points[route[i+1]-1][1];
        while startr != endr:
            graph.append((time,startr,startc));
            if startr<endr:
                startr += 1;
            else:
                startr -= 1;
            time += 1;
        while startc != endc:
            graph.append((time,startr,startc));
            if startc<endc:
                startc += 1;
            else:
                startc -= 1;
            time += 1;
    graph.append((time,startr,startc));
            
                
            
def solution(points, routes):
    answer = 0;
    graph = [];
    for route in routes:
        move(graph,points,route);
    temp = Counter(graph);
    for i in temp.values():
        if i>=2:
            answer += 1;
    return answer;
                
        