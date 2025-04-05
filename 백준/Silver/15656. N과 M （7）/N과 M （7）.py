import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
arr = list(map(int,input().split()));
arr.sort();

def backtracking(cur, depth):
  if len(cur) == m:
    print(*cur);
    return;
  for num in arr:
    cur.append(num);
    backtracking(cur,depth+1);
    cur.pop();
backtracking([],1);