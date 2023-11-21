def binary_search(arr,target,start,end):
  while start<=end:
    mid  = (start+end)//2;
    if arr[mid] == target:
      return 1;
    if arr[mid] < target:
      start = mid+1;
    elif arr[mid]> target:
      end = mid-1;
  return 0;

n = int(input());
arr1 = list(map(int,input().split()));
m = int(input());
arr2 = list(map(int,input().split()));
arr1.sort();

for i in range(len(arr2)):
  print(binary_search(arr1,arr2[i],0,n-1),end=' ');