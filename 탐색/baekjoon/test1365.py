import sys;
def binary_search(arr,target,start,end):
  mid = (start+end)//2
  if start>end:
    return start;
  if target<arr[mid]:
    end = mid-1;
    return binary_search(arr,target,start,end);
  else:
    start = mid+1;
    return binary_search(arr,target,start,end);
  

n = int(input());
arr = list(map(int,sys.stdin.readline().split()));
newarr = [arr[0]]
for i in range(1,n):
  if arr[i] > newarr[-1]:
    newarr.append(arr[i]);
  else:
    count = 0;
    j = i+1;
    
      
    index = binary_search(newarr,arr[i],0,len(newarr)-1);
    newarr[index] = arr[i];
print(len(arr)-len(newarr));