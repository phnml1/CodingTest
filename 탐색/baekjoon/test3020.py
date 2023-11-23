#나의 비효율적인 풀이 (백준에서 답은 맞음)
import sys;
def binary_search(arr, target, start, end):
  mid = (start+end)//2;
  while start<=end:
    mid = (start+end)//2;
    if arr[mid] == target:
      return mid;
    if arr[mid]<target:
      start = mid+1;
    if arr[mid]>target:
      end = mid-1;
  while arr[mid]<target and mid<len(arr)-1:
    mid += 1;
  return mid;
    
n,h = map(int,input().split());
arr1,arr2 = [],[];
for i in range(n):
  if i%2 == 0:
    arr1.append(int(sys.stdin.readline()));
  else:
    arr2.append(int(sys.stdin.readline()));
arr1.sort();
arr2.sort();
obstacles = [];
for i in range(h-2):
  cnt=0;
  minl = binary_search(arr1, i+2, 0,int(n/2-1));
  minh = binary_search(arr2,h-(i+1),0,int(n/2-1));
  if minl == len(arr1)-1 and arr1[minl]<i+2 :
    cnt += 0;
  else:
    result = arr1[minl];
    while result==arr1[minl]:
      if minl!=0:
        if arr1[minl-1]==arr1[minl]:
          minl-=1;
        else:
          break;
      else:
        break;
    cnt += int(n/2) - minl;
  if minh == len(arr2)-1 and arr2[minh]<h-(i+1):
    cnt+=0
  else:
    result = arr2[minh];
    while result==arr2[minh]:
      if minh!=0:
        if arr2[minh-1]==arr2[minh]:
          minh-=1;
        else:
          break;
      else:
        break;
    cnt += int(n/2)-minh;
  
    
  obstacles.append(cnt);
  
obstacles.sort();
i=0;
mincnt=0;
minnum = obstacles[0];
while obstacles[i]==obstacles[0]:
  mincnt += 1;
  i+=1;
if obstacles[0]==int(n/2):
  mincnt+=2;
elif obstacles[0]>int(n/2):
  mincnt=2;
  minnum = int(n/2)
print(minnum,mincnt);

#모범답안(애초에 최소가 나오도록 찾고 애초에 불필요하게 2구간부터 하지않음)
# import sys

# input = sys.stdin.readline

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return left

# n, h = map(int, input().split())

# up, down = [], []
# for i in range(n):
#     if i % 2 == 0:
#         up.append(int(input()))
#     else:
#         down.append(int(input()))

# up.sort()
# down.sort()

# obs_cnt, sec_cnt = n, 0
# for i in range(1, h + 1):
#     up_cnt = len(up) - binary_search(up, h - i + 0.5)
#     down_cnt = len(down) - binary_search(down, i - 0.5)
#     total_cnt = up_cnt + down_cnt

#     if obs_cnt == total_cnt:
#         sec_cnt += 1
#     elif obs_cnt > total_cnt:
#         obs_cnt = total_cnt
#         sec_cnt = 1

# print(obs_cnt, sec_cnt)

