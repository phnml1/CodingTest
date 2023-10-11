#내풀이
num = int(input());
homes = []
homes_num = {};
result = 0;
#단지안의 집들의 개수를 구하기위한 고유번호
homes_index = 0;
for i in range(num):
    homes.append(list(map(int,input())));
visited = [[False]*num for _ in range(num)];


def dfs(r,c,homes_index):
    dc = [1,-1,0,0];
    dr = [0,0,1,-1];
    visited[r][c] = True;
    if homes_index not in homes_num:
        homes_num[homes_index] = 1;
    else:
        homes_num[homes_index]+=1;
    for i in range(4):
        cur_r,cur_c = r+dr[i],c+dc[i];
        if 0<=cur_r<num and 0<=cur_c<num:
            if homes[cur_r][cur_c] == 1 and not visited[cur_r][cur_c]:
                dfs(cur_r,cur_c,homes_index);

for i in range(num):
    for j in range(num):
        if homes[i][j] ==1 and not visited[i][j]:
            dfs(i,j,homes_index);
            homes_index += 1;
            result += 1;
print(result);
homes_num = list(homes_num.values())
homes_num.sort();
for i in range(len(homes_num)):
    print(homes_num[i]);
    
    