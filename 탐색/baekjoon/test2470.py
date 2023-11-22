import sys;

def binary_search(arr,target,start,end):
  result = 0;
  while start<=end:
    mid = (start + end)//2;
    if arr[mid] <= target:
      start = mid+1;
      result = mid;
    else:
      end = mid-1;
  return result;



n = int(input());
arr = list(map(int,sys.stdin.readline().split()));
arr.sort();
i=0;
min = sys.maxsize;
result1,result2 = 0,0;
for i in range(n):
  find = -arr[i]
  index = binary_search(arr,find,0,n-1);
  right = sys.maxsize;
  target = arr[index] + arr[i];
  if target == 0:
    min = 0;
    result1 = i;
    result2 = index;
    break;
  if index+1 < n-1:
    right = arr[index+1]+arr[i];
  if abs(right)<abs(target):
      target = right;
      index = index+1;
  if index == i:
    continue;
  if abs(target)<abs(min):
    min = target;
    result1 = i;
    result2 = index;
  i+=1;
result = [arr[result1],arr[result2]];
result.sort();
print(result[0], result[1]);