import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
arr = list(map(int,input().split()));
arr.sort();
results = [];
def backtracking():
  check = 0;
  if len(results) == m:
    print(*results);
    return;
  for i in range(n):
    if check != arr[i]:
      results.append(arr[i]);
      check = arr[i]
      backtracking();
      results.pop();
backtracking();