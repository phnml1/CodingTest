from collections import deque;
m,n = map(int, input().split());
iceArray = []
result = 0
for i in range(m):
    iceArray.append(list(map(int,input())))
    
def bfs(y,x):
    dy = [0,1,-1,0];
    dx = [1,0,0,-1];
    iceArray[y][x] = 1;
    queue = deque();
    queue.append((y,x));
    
    while queue:
        cury,curx = queue.popleft();
        for i in range(4):
            if cury+dy[i]>=0 or cury+dy[i]<m or dx[i]+curx>=0 or dx[i]+curx<n:
                if iceArray[cury+dy[i]][curx+dx[i]] == 0:
                    iceArray[cury+dy[i]][curx+dx[i]] = 1;
                    queue.append((cury+dy[i],curx+dx[i]))
#책풀이                             
def dfs(y,x):
    if x<=-1 or x>=m or y<=-1 or y>=n:
        return False
    if iceArray[y][x] == 0:
        iceArray[y][x] = 1
        dfs(y,x)
        dfs(y-1,x-1)
        dfs(y+1,x)
        dfs(y,x+1)
        return True
    return False       
                
        

for y in range(m):
    for x in range(n):
        if iceArray[y][x] == 0:
            dfs(x,y);
            result +=1                
print(result)
    