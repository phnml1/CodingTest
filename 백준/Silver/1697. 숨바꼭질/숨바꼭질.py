from collections import deque

max_location = 100000;
n,k = map(int,input().split());
result = 1e9;
queue = deque();
visited = [1e9 for _ in range(max_location+1)];
queue.append((0,n));
while queue:
    t,x = queue.popleft();
    if x == k:
        print(t);
        break;
    for newx in ((x-1,x+1,x*2)):
        if 0<=newx<=max_location and t+1<visited[newx]:
            visited[newx] = t+1;
            queue.append((t+1,newx));