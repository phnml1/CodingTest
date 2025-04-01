import sys
input = sys.stdin.readline;

n = int(input());
arr = [];
for _ in range(n):
  arr.append(list(map(int,input().split())));
result = [0,0];
def recur(x,y,num):
  prev = arr[x][y];
  flag = True;
  if num == 1:
    result[prev] += 1;
    return;
  for i in range(x,x+num):
    for j in range(y,y+num):
      if prev != arr[i][j]:
        flag = False;
        break;
  if flag:
    result[prev] += 1;
  else:
    for i in range(2):
      for j in range(2):
        recur(x+num//2*i,y+num//2*j,num//2);
recur(0,0,n);
for i in range(2):
  print(result[i]);