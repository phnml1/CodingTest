n = int(input());
arr = list(map(int,input().split()));

def binary_search(arr, start, end):
  mid = (start + end) // 2
  if start > end:
    return -1
  if arr[mid] == mid:
    return mid;
  elif arr[mid] <mid:
    return binary_search(arr,mid+1,end);
  else:
    return binary_search(arr,start,mid-1);

print(binary_search(arr,0,n-1));