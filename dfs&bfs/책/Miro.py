from collections import deque

n, m = map(int, input().split())
graph = []

result = 0
for i in range(n):
    graph.append(list(map(int, input())))

def bfs():
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    result = 0
    queue = deque()
    queue.append((0, 0, 1))
    
    while queue:
        x, y, cur_len = queue.popleft()

        if x == m - 1 and y == n - 1:
            return cur_len

        for i in range(4):
            cur_x, cur_y = x + dx[i], y + dy[i]
            
            if 0 <= cur_x < m and 0 <= cur_y < n and graph[cur_y][cur_x] != 0:
                graph[cur_y][cur_x] = 0
                queue.append((cur_x, cur_y, cur_len + 1))

print(bfs())
