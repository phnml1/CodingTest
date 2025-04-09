import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
arr = list(map(int,input().split()));
arr.sort();
visited= [0] *n;
results = [];
def backtracking(index):
  check = 0;
  if len(results) == m:
    print(*results);
    return;
  for i in range(index,n):
    if check != arr[i] and visited[i] == 0:
      results.append(arr[i]);
      visited[i] = 1;
      check = arr[i]
      backtracking(i+1);
      results.pop();
      visited[i] = 0;
backtracking(0);