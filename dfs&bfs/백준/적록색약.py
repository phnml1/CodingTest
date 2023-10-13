import sys

n = int(input())
arr = []
arr2 = []
count1 = 0
count2 = 0
for _ in range(n):
    arr.append(list(input()))

visited1 = [[False]*n for _ in range(n)]
visited2 = [[False]*n for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

sys.setrecursionlimit(10**6)  # 필요에 따라 제한을 조정하세요

def dfs(i, j, visited):
    visited[i][j] = True
    for a in range(4):
        cur_r = i + dr[a]
        cur_c = j + dc[a]
        if 0 <= cur_r < n and 0 <= cur_c < n and not visited[cur_r][cur_c]:
            if arr[i][j] == arr[cur_r][cur_c]:
                dfs(cur_r, cur_c, visited)

def count_connected_components(visited):
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, visited)
                count += 1
    return count

count1 = count_connected_components(visited1)
count2 = count_connected_components(visited2)

print(count1, count2)

