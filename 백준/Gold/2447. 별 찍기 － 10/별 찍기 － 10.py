import sys
input = sys.stdin.readline;

n = int(input());
arr = [[' ' for _ in range(n)] for _ in range(n)];
def recur(x,y,num):
  if num== 1:
    arr[x][y] = '*'
    return;
  for i in range(3):
    for j in range(3):
      if i==1 and j==1:
        continue;
      recur(x+num//3*i, y+num//3*j, num//3);
recur(0,0,n);
for i in range(n):
  for j in range(n):
    print(arr[i][j],end='');
  print();