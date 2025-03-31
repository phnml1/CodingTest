import sys
input = sys.stdin.readline;

n = int(input());
arr = []
result = [0,0,0];
for _ in range(n):
  arr.append(list(map(int,input().split())));
def cur(x,y,n):
  prev = arr[x][y];
  if n==1:
    result[arr[x][y]] += 1;
    return;
  flag = True;
  for i in range(x,x+n):
    for j in range(y,y+n):
      if prev != arr[i][j]:
        flag = False;
        break;
  if flag:
    result[prev] += 1;
  else:
    for a in range(3):
      for b in range(3):
        cur(x+a*n//3,y+b*n//3,n//3); 
    
cur(0,0,n);
for i in range(-1,2):
  print(result[i]);
