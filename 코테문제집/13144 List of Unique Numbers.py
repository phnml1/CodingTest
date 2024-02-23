n = int(input())
s = list(map(int,input().split()))
re=0
st,en = 0,0
visited = [False for _ in range(100001)];

while st<n and en<n:
  if not visited[s[en]]:
    visited[s[en]] = True; 
    en += 1;
    re += en-st # en을끝으로 하는 부분수열 예를들어, 4면 4, 3,4, 2,3,4, 1,2,3,4,
  else:
    visited[s[st]] = False;
    st += 1;
    
    
print(re)#결과 출력