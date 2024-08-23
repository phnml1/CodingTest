import sys;
input = sys.stdin.readline;
#리스트 슬라이싱
N,d,k,c = map(int,input().split());
result = 0;
seusis = [];

for _ in range(N):
  seusis.append(int(input()));
seusis.extend(seusis[:k+1]);

for i in range(N):
  tmp = set(seusis[i:i+k]);
  tmp.add(c);
  result = max(result,len(tmp));
print(result);

    
  