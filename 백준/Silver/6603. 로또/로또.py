import sys
input = sys.stdin.readline;

def backtracking(arr,index,results):
  if len(results) == 6:
    print(*results);
    return;
  for i in range(index, len(arr)):
    results.append(arr[i]);
    backtracking(arr,i+1,results);
    results.pop();
while True:
  i = list(map(int,input().split()));
  if i[0] == 0:
    break;
  else:
    n = i[0];
    arr = i[1:];
    backtracking(arr,0,[]);
    print();
  


