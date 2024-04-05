import sys
input = sys.stdin.readline;
n,k = map(int,input().split());
arr = list(map(int,input().split()));
multi = [];
result = 0;
for i in range(len(arr)):
  cur = arr[i];
  if len(multi)<n and cur not in multi:
    multi.append(cur);
  elif len(multi) == n and cur not in multi:
    if i == len(arr)-1:
      result += 1;
    else:
      far_index = -1;
      index = 0;
      for j in range(len(multi)):
        if multi[j] not in arr[i+1:]:
          multi[j] = cur;
          result += 1;
          far_index = -1;
          break;
        else:
          if far_index < arr[i+1:].index(multi[j]):
            far_index = arr[i+1:].index(multi[j]);
            index = j;
      if far_index != -1:
        multi[index] = cur;
        result += 1;
        
print(result);