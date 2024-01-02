#나의 기나긴 코드
from itertools import combinations;
import copy;
n = int(input());
data,blanks,teachers = [],[],[];

for i in range(n):
  arr = list(map(str,input().split()));
  data.append(arr);

for i in range(n):
  for j in range(n):
    if data[i][j] == 'X':
      blanks.append((i,j));
    if data[i][j] == 'T':
      teachers.append((i,j));
def dfs(data,i,j):
  temp_i = i;
  while temp_i> 0:
    temp_i -= 1;
    if data[temp_i][j] == 'S':
      return False
    if data[temp_i][j] == 'O':
      break;
  temp_i = i;
  while temp_i<n-1:
    temp_i += 1;
    if data[temp_i][j] == 'S':
      return False
    if data[temp_i][j] == 'O':
      break;
  temp_j = j;
  while temp_j<n-1:
    temp_j += 1;
    if data[i][temp_j] == 'S':
      return False
    if data[i][temp_j] == 'O':
      break;
  temp_j = j;
  while 0<temp_j:
    temp_j-=1;
    if data[i][temp_j] == 'S':
      return False
    if data[i][temp_j] == 'O':
      break;
  return True;
all_possible_blanks = list(combinations(blanks,3));
for possible_blanks in all_possible_blanks:
  watched = True;
  temp_data = copy.deepcopy(data);
  for x,y in possible_blanks:
    temp_data[x][y] = 'O';
  for x,y in teachers:
    watched = dfs(temp_data,x,y);
    if watched == False:
      break;
  if watched == True:
    break;
if watched:
  print('YES');
else:
  print('NO');
  
