import sys

n,c = map(int,sys.stdin.readline().split());
arr = []
for i in range(n):
  arr.append(int(sys.stdin.readline()));
arr.sort();
start = 0;
end = arr[-1] - arr[0];
result = -1
while start<=end:
  dist = int((start+end)/2)
  cnt = 1
  val = arr[0]
  for i in range(1,len(arr)):
    if arr[i]-val >= dist:
      val = arr[i]
      cnt+=1
  if cnt >= c:
    result = dist
    start = dist+1
  else:
    end = dist-1
print(result);
  