from collections import deque
import sys;
input = sys.stdin.readline;
n,k = map(int,input().split());
MAX_SIZE = 100000;
visited = [1e9 for _ in range(MAX_SIZE+1)];
def bfs(visited):
  visited[n] = 0;
  queue = deque()
  queue.append((0,n,[n]));
  if n>k:
    return n-k,[int(x) for x in range(n,k-1,-1)];
  while queue:
    cost,num,nums  = queue.popleft();
    if cost < visited[num]:
      visited[num] = cost;
    if num == k:
      return cost,nums;
    
    for next in [num+1,num-1,num*2]:
      if 0<=next<=MAX_SIZE:
        if cost+1 < visited[next]:
          visited[next] = cost+1;
          r = nums + [next];
          queue.append((cost+1,next,r));
            
cost,nums = bfs(visited)
print(cost);
for num in nums:
  print(num, end = ' ');