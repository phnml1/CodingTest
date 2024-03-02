from collections import deque
import sys
input = sys.stdin.readline;
arr = [];
result = 0
for _ in range(4):
  arr.append(deque(list(map(int,input().rstrip()))));
k = int(input());
for i in range(k):
  rot = [0,0,0,0]
  n,r = map(int,input().split());
  index = n-1;
  rot[n-1] = r;
  while index>0:
    if arr[index-1][2] != arr[index][6] and rot[index] != 0:
      rot[index-1] = -rot[index];
    index-=1;
    if rot[index] == 0:
      break;
  index = n-1;
  while index<3:
    if arr[index+1][6] != arr[index][2] and rot[index] != 0:
      rot[index+1] = -rot[index];
    index+=1;
    if rot[index] == 0:
      break;
  for i in range(len(rot)):
    arr[i].rotate(rot[i])
for i in range(len(arr)):
  result += (arr[i][0]*(2**i))
print(result);