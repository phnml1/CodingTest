def solution(n, results):
    answer = 0
    floyd = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for result in results:
        floyd[result[0]][result[1]] = 1;
        floyd[result[1]][result[0]] = -1;
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if floyd[i][k] == 1 and floyd[k][j] == 1:
                    floyd[i][j] = 1;
                if floyd[i][k] == -1 and floyd[k][j] == -1:
                    floyd[i][j] = -1;
    for i in range(1,n+1):
        if floyd[i].count(1) + floyd[i].count(-1) == n-1:
            answer += 1;
    return answer