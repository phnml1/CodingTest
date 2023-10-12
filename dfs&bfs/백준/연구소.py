from collections import deque
from itertools import *
import copy

r,c = map(int, input().split())
arr,blanks,possible_walls,testarr=[],[],[],[];
wall_num = 0
result = 9999;
for i in range(r):
    arr.append(list(map(int, input().split())));
for i in range(r):
    for j in range(c):
        if arr[i][j] == 0:
            blanks.append([i,j]);
        if arr[i][j] == 1:
            wall_num +=1;
possible_walls = list(combinations(blanks,3));

def bfs(i,j,testarr):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    count = 0
    queue = deque()
    queue.append((i,j));
    testarr[i][j] = 3
    while queue:
        cur_r,cur_c = queue.popleft()
        count +=1;
        for a in range(4):
            if 0<=cur_r+dr[a]<r and 0<=cur_c+dc[a]<c:
                if testarr[cur_r+dr[a]][cur_c+dc[a]] == 0 or testarr[cur_r+dr[a]][cur_c+dc[a]] == 2:
                    testarr[cur_r + dr[a]][cur_c+dc[a]] = 3;
                    queue.append((cur_r+dr[a],cur_c+dc[a]));
    return count;

for pwall in possible_walls:
    testarr = copy.deepcopy(arr);
    cur_result = 0;
    for wall in pwall:
        testarr[wall[0]][wall[1]] = 1;
    for i in range(r):
        for j in range(c):
            if testarr[i][j] == 2:
                cur_result += bfs(i,j,testarr);
    result = min(result,cur_result);
print(r*c - result - (wall_num+3));
