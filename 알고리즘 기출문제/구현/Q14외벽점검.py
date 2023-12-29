# p337

from itertools import permutations
# 인터넷
def solution(n,weak,dist):
  # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
  length = len(weak);
  cand = []
  for i in range(length):
    weak.append(weak[i]+n);
  answer = len(dist) + 1 #투입할 친구 수의 최솟값을 찾아야함, len(dist)+1로 초기화
  
  # 0부터 length-1까지의 위치를 각각 시작점으로 설정
  for i, start in enumerate(weak):
    for friends in permutations(dist): # 순열 이용
      count = 1
      position = start
      # 친구 조합 배치
      for friend in friends:
        position += friend
        # 끝 포인트까지 도달 못했을 때
        if position < weak[i+length-1]:
          count += 1
          # 현재위치보다 멀리있는 취약지점 중 가장 가까운 위치로
          position = [w for w in weak[i+1:i+length] if w>position][0]
        else:
          cand.append(count)
          break
  return min(cand) if cand else -1;

# 책 풀이

def solution2(n,weak,dist):
  # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
  length = len(weak);
  for i in range(length):
    weak.append(weak[i]+n);
  answer = len(dist) + 1 #투입할 친구수의 최솟값을 찾아야하므로
  # 0부터 length-1 까지의 위치를 각각 시작점으로 설정
  for start in range(length):
    # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
    for friends in list(permutations(dist, len(dist))):
      count = 1 #투입할 친구의 수
      # 해당 친구가 점검할 수 있는 마지막 위치
      position = weak[start] + friends[count - 1];
      # 시작점부터 모든 취약 지점을 확인
      for index in range(start,start+length):
        # 점검할 수 있는 위치를 벗어나는 경우
        if position < weak[index]:
          count += 1
          if count >len(dist): # 더 투입이 불가능하다면 종료
            break
          position  = weak[index] + friends[count-1]
      answer = min(answer,count) # 최솟값 계산
      
    if answer > len(dist):
      return -1
    return answer