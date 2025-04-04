import sys
input = sys.stdin.readline;

n,m = map(int,input().split());

def backtracking(arr,i,r):
  if r==m:
    print(' '.join(arr));
    return;
  else:
    for a in range(i,n-(r-m)):
      arr.append(str(a));
      backtracking(arr,a,r+1);
      arr.pop();
for i in range(1,n+1):
  backtracking([str(i)],i,1);
  
