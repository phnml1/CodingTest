import sys;
input = sys.stdin.readline;
from collections import deque

n,k = map(int,input().split());
arr = deque(list(map(int,input().split())));

answer = 0;
robots = deque([False]*n);
while True:
  answer += 1;
  arr.rotate(1);
  robots.rotate(1);
  robots[n-1] = False;
  for i in range(n-2,-1,-1):
    if robots[i] and robots[i+1] == False and arr[i+1]>0:
      robots[i+1] = True;
      robots[i] = False;
      arr[i+1] -= 1;
  robots[n-1] = False;     
  if arr[0] > 0 and robots[0] == False:
    robots[0] = True;
    arr[0] -=1;
  if arr.count(0)>=k:
      break;
print(answer);