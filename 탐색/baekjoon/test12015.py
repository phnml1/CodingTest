def binary_search(ar,target,start,end):
  while start<=end:
    mid = (start+end)//2;
    if target == ar[mid]:
      return mid;
    if target<=ar[mid]:
      end = mid-1;
    if target>ar[mid]:
      start = mid+1;
  return start;
n = int(input());
arr = list(map(int,input().split()));
ln = [arr[0]];
for case in arr:
  if ln[len(ln)-1] < case:
    ln.append(case);
  else:
    # 수열을 연장하기위해 작은값이라도 넣는것
    ln[binary_search(ln,case,0,len(ln)-1)] = case;
print(len(ln));
    