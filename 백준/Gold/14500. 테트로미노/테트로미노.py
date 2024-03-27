import copy
n,m = map(int,input().split());
arr = []
result = 0
for i in range(n):
  arr.append(list(map(int,input().split())));
tetriminos = [[1,1,[(1,0),(2,0),(3,0)]],[1,0,[(1,0),(0,1),(1,1)]],[2,3,[(1,0),(2,0),(2,1)]],[2,1,[(1,0),(1,1),(2,1)]],[1,3,[(0,1),(1,1),(0,2)]]]

def rotated(array_2d):
    n = len(array_2d) # 행 길이
    m = len(array_2d[0]) # 열 길이 
    result = [[0] * n for _ in range(m)] # 회전한 결과를 표시하는 배열

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = array_2d[i][j]
    return result

def mirror_horizontally(array):
    n = len(array)
    for i in range(n):
        array[i] = array[i][::-1]

    return array
def tetrimino(arr,tets):
  result = 0
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      count = 0;
      count += arr[i][j]
      for x,y in tets:
        if i+x>=len(arr) or j+y>=len(arr[0]):
          continue;
        else:
          count += arr[i+x][j+y];
      result = max(result,count);
  return result;
for tet in tetriminos:
  for i in range(tet[0]):
    temp = copy.deepcopy(arr);
    if i == 1:
      temp = mirror_horizontally(temp);
    result = max(result,tetrimino(temp,tet[2]));
    for i in range(tet[1]):
      temp = rotated(temp)
      result = max(result,tetrimino(temp,tet[2]));
    
print(result);