import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
arr = list(map(int,input().split()));
arr.sort();
results = [];
def backtracking(index):
  check = 0;
  if len(results) == m:
    print(*results);
    return;
  for i in range(index,n):
    if check != arr[i]:
      results.append(arr[i]);
      check = arr[i]
      backtracking(i);
      results.pop();
backtracking(0);