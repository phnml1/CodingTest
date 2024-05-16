from collections import deque
def solution(land):
    answer = 0
    queue = deque();
    d = [(1,0),(0,1),(-1,0),(0,-1)];
    dic = {}            
    def bfs(land,i,j,num):
        count = 0;   
        queue.append((i,j));
        land[i][j] = num;
        while queue:
            r,c = queue.popleft();
            count += 1;
            for n in range(4):
                dx,dy = d[n];
                next_r, next_c = r+dx,c+dy;
                if 0<=next_r<len(land) and 0<=next_c<len(land[0]):
                    if land[next_r][next_c] == 1:
                        land[next_r][next_c] = num;
                        queue.append((next_r,next_c));
        return count;
    num = 2;
    for i in range(len(land)): 
        for j in range(len(land[0])):     
            if land[i][j] == 1 and land[i][j] == 1:
                dic[num] = bfs(land,i,j,num);
                num+=1;
    for i in range(len(land[0])):
      visit = [];
      result = 0;
      for j in range(len(land)): 
        if land[j][i] != 0 and land[j][i] not in visit:
          result += dic[land[j][i]];
          visit.append(land[j][i])
      answer = max(result,answer);
                                
    return answer
  
print(solution(	[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))