# p369
# n,x = map(int,input().split());
# data = list(map(int,input().split()));

# def binary_search(data,target,start,end):
#   if start>end:
#     return None
#   mid = (start + end) // 2;
#   if data[mid]<target:
#     return binary_search(data,target,mid+1,end);
#   if data[mid] == target:
#     return mid;
#   else:
#     return binary_search(data,target,start,mid-1);

# found_index = binary_search(data,x,0,n-1)
# if found_index == None:
#   print(-1);
# else:
#   index = found_index
#   result = 1;
#   while data[index]==x:
#     index -= 1;
#     if data[index] == x:
#       result += 1;
#   index = found_index
#   while data[index]==x:
#     index += 1;
#     if data[index]==x:
#       result += 1;
#   print(result);

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메소드
def count_by_value (array,x):
  n = len(array)
  
  a = first(array,x,0,n-1)
  
  if a == None:
    return 0
  
  b = last(array,x,0,n-1)
  
  return b - a + 1;

# 처음 위치를 찾는 이진 탐색 메소드
def first(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2;
  # 해당 값을 가진 원소중에서 가장 왼쪽에 있을 때만 반환
  if ((mid == 0) or array[mid-1] < target) and array[mid] == target:
    return mid
  # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
  elif array[mid] >= target:
    return first(array, target, start, mid-1);
  else:
    return first(array, target, mid+1, end);
  
# 마지막 위치를 찾는 이진 탐색 메소드
def last(array, target, start, end):
  if start> end:
    return None
  mid = (start+end)//2
  # 해당 값을 가진 원소중에서 가장 오른쪽에 있을때만
  if ((mid==n-1) or array[mid+1] > target) and array[mid] == target:
    return mid
  # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return last(array, target, start, mid-1);
  # 중간점의 값 보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
  else:
    return last(array, target, mid + 1,end);

n,x = map(int,input().split()) # 데이터의 개수 N, 찾고자 하는 값 x를 입력받기
array = list(map(int,input().split())); # 전체 데이터 입력받기

# 값이 x인 데이터의 개수 계산
count = count_by_value(array,x);

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
  print(-1)
else:
  print(count);
