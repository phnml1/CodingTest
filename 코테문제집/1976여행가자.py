from collections import deque


n = int(input());
m = int(input());
arr = [[] for i in range(n+1)]
result = 'YES';
for i in range(1,n+1):
  nums = list(map(int,input().split()));
  for j in range(1,n+1):
    if nums[j-1]==1:
      arr[j].append(i);
des = list(map(int,input().split()));
q = deque();
start = des[0]
visited = [False for _ in range(n+1)];
q.append(start);
while q:
 cur_node = q.popleft();
 visited[cur_node] = True
 for node in arr[cur_node]:
   if visited[node] == False:
    q.append(node);
    
for i in des:
  if visited[i] == False:
    result = 'NO';
    break;
print(result);