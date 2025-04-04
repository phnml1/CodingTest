import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
arr = list(map(int,input().split()));
arr.sort();
def backtracking(arr,cur,r):
  if r==m:
    print(' '.join(cur))
    return;
  else:
    for num in arr:
      i = arr.index(num)
      cur.append(str(arr.pop(i)));
      backtracking(arr,cur,r+1);
      arr.insert(i,num);
      cur.pop();
backtracking(arr,[],0);