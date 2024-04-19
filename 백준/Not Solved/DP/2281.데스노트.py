import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
name = [int(input()) for _ in range(n)]

maxNum = m*m*n;
dp = [maxNum] * (n+1);
dp[n] = 0;
# dp[index]는 index+1번째의 이름을 '새로운 줄' 에 작성할 때, 남은 공간들의 제곱합의 최소를 저장한다.
def note(index):
    # 이미 갱신된 dp값
    if dp[index]<maxNum:
        return dp[index];
    
    remain = m - name[index];
    
    for i in range(index+1,n+1):
        if remain>=0:
            if i==n:
                dp[index] = 0;
                break;
            dp[index] = min(dp[index],remain*remain+note(i));
            remain -= name[i] + 1;
    
    return dp[index];

print(note(0));