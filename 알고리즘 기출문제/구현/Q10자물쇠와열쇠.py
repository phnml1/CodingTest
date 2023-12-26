# p327 1
def rotate_90_degree(key):
  n = len(key)
  m = len(key[0])
  result = [[0]*n for _ in range(m)];
  #90도
  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = key[i][j];
  return result;

def check(newlock):
  lock_length = len(newlock) // 3;
  for i in range(lock_length, lock_length*2):
    for j in range(lock_length, lock_length*2):
      if newlock[i][j] != 1:
        return False
  return True;

def solution(key,lock):
  n = len(lock);
  m = len(key);
  newlock = [[0] * (n*3) for _ in range(n*3)];
  #새로운 자물쇠의 중앙 부분에 기존자물쇠넣기
  for i in range(n):
    for j in range(n):
      newlock[i+n][j+n] = lock[i][j];

  for rotation in range(4):
    key = rotate_90_degree(key); #열쇠 회전
    #중앙 위치 까지만
    for x in range(n*2):
      for y in range(n*2):
        for i in range(m):
          for j in range(m):
            newlock[x+i][y+j] += key[i][j]; 
        if check(newlock) == True:
          return True
        # 자물쇠에서 열쇠빼기
        for i in range(m):
          for j in range(m):
            newlock[x+i][y+j] -= key[i][j];
  return False
  

print(solution([[0,0,0],[1,0,0],[0,1,1]],[]))