# O(M^3)
#일일히, 전체 구조물을 확인하며, 규칙을 확인

# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
  for x,y,stuff in answer:
    if stuff == 0: #설치된 것이 '기둥'인경우
      # 바닥위 혹은 보의 한쪽 끝부분위 혹은 다른기둥위라면 정상
      if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
        continue
      return False
    elif stuff == 1: #설치된 것이 보인경우
      #한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
      if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
        continue
      return False
    return True

def solution (n, build_frame):
  answer = []
  for frame in build_frame:
    x,y,stuff,operate = frame
    if operate ==0: #삭제시
      answer.remove([x,y,stuff]) # 일단 삭제를 해보고
      if not possible(answer): # 가능한 구조물인지 확인
        answer.append([x,y,stuff]) # 가능한 구조물이 아니면 다시 설치
    if operate == 1:
      answer.append([x,y,stuff])
      if not possible(answer): #가능한 구조물인지 확인
        answer.remove([x,y,stuff]); # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) #정렬된 결과 반환