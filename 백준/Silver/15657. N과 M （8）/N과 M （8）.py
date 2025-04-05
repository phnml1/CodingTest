import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
arr = list(map(int,input().split()));
arr.sort();

def backtracking(cur, index):
  if len(cur) == m:
    print(*cur);
    return;
  for i in range(index,len(arr)):
    backtracking(cur+[arr[i]],i);
backtracking([],0);