def binary_search(array,target,start,end):
  mid = (start+end)//2;
  if start>end:
    return None;
  if array[mid] == target:
    return mid;
  elif array[mid] > target:
    return binary_search(array, target,start,mid-1);
  else:
    return binary_search(array, target,mid+1,end);


n = int(input());
arr1 = list(map(int,input().split()));
arr1.sort();
m = int(input());
arr2 = list(map(int,input().split()));
for i in range(len(arr2)):
  if binary_search(arr1,arr2[i],0,n-1)!=None:
    print('yes', end=' ');
  else:
    print('no', end= ' ');
    

# N( 가게의 부품 개수)을 입력받기 
n = int(input()) 
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록 
array = set(map(int, input() .split() )) 
# M( 손님이 확인 요청한 부품 개수)을 입력받기 
m = int(input()) 
# 손님이 확인 요청한 전체 부풍 번호를 공백으로 구분하여 입력 
x = list(map(int, input() .split())) 
# 손님이 확인 요청한 부품 번호를 하나씩 확인 
for i in x: 
# 해당 부품이 존재하는지 확인 
  if i in array: 
    print('yes', end=' '); 
  else: 
    print ('no', end =' ');
