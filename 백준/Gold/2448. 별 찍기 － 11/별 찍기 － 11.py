import sys
input = sys.stdin.readline;

n = int(input());
garo = 5*n//3 + n//3-1
arr = [[' ' for _ in range(garo) ] for _ in range(n)];
def recur(x,y,num):
  if num == 3:
    arr[x][y] = '*'
    arr[x+1][y-1] = '*'
    arr[x+1][y+1] = '*';
    for i in range(5):
      arr[x+2][y-2+i]= '*';
    return;
  recur(x,y,num//2);
  recur(x+num//2,y-num//2,num//2);
  recur(x+num//2,y+num//2,num//2);    
  
recur(0,n-1,n);

for i in range(n):
  for j in range(garo):
    print(arr[i][j], end = '');
  print();