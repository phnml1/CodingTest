# def rice_cake_search(arr,target,start,end):
#   mid = start+end//2;
#   newarr = []
#   sum_of_newarr = 0;
#   result = arr[mid];
#   for i in range(len(arr)):
#     if (arr[i]-arr[mid])>0:
#       newarr.append(arr[i] - arr[mid]);
#     else:
#       newarr.append(0);
#   sum_of_newarr = sum(newarr);
#   if sum_of_newarr>target:
#     while sum_of_newarr>=target:
#       newarr = []
#       result += 1
#       for i in range(len(arr)):
#         if (arr[i]-result)>0:
#           newarr.append(arr[i] - result);
#         else:
#           newarr.append(0);
#       sum_of_newarr = sum(newarr);
#     result -= 1
#   elif sum_of_newarr< target:
#     while sum_of_newarr<target:
#       newarr = []
#       result -= 1
#       for i in range(len(arr)):
#         if (arr[i]-result)>0:
#           newarr.append(arr[i] - result);
#         else:
#           newarr.append(0);
#       sum_of_newarr = sum(newarr);
  # return result
def rice_cake_search(arr,m,start,end):
  mid = (start+end)//2;
  newarr = []
  if start>end:
    return mid;
  for i in range(len(arr)):
    if (arr[i]-mid)>0:
      newarr.append(arr[i]-mid);
    else:
      newarr.append(0);
  sum_of_newarr = sum(newarr);
  if sum_of_newarr<m:
    return rice_cake_search(arr,m,start,mid-1);
  elif sum_of_newarr>m:
    return rice_cake_search(arr,m,mid+1,end);
  else:
    return mid;

    
h,m = map(int,input().split());
arr = list(map(int,input().split()));
arr.sort();
# print(rice_cake_search(arr,m,0,arr[h-1]));

start = 0
end = max(arr)

result = 0
while(start<=end):
  total = 0
  mid = (start+end)//2
  for x in arr:
    if x>mid:
      total += x-mid;
  if total>=m:
    start = mid+1
    result=mid
  else:
    end = mid-1
print(result);