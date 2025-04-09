import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
arr = list(map(int,input().split()));
arr.sort();
visited= [0] *n;
results = [];
def backtracking():
  check = 0;
  if len(results) == m:
    print(*results);
    return;
  for i in range(n):
    if check != arr[i] and visited[i] == 0:
      results.append(arr[i]);
      visited[i] = 1;
      check = arr[i]
      backtracking();
      results.pop();
      visited[i] = 0;
backtracking();