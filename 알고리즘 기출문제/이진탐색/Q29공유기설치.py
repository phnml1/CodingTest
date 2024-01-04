# p 372 (복습 필수)
n,c = map(int,input().split());
arr = []
for i in range(n):
  arr.append(int(input()));
arr.sort();

start = arr[1] - arr[0] # 집의 좌표 중에 가장 작은 값
end = arr[-1] - arr[0] # 집의 좌표중에 가장 큰 값
result = 0

while (start <= end):
  mid = (start + end) // 2
  value = arr[0]
  count = 1
  # 현재의 mid값을 이용해 공유기 설치
  for i in range(1,n): # 앞에서부터 차근차근 설치
    if arr[i] >= value + mid:
      value = arr[i]
      count += 1
  if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
    start = mid + 1
    result = mid # 최적의 결과 저장
  else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
    end = mid - 1
      
print(result);