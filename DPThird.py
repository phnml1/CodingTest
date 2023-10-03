cost = [10,15,20,17,1]
memo = {}
def dpTopBottom(n):
    if n==0:
        return 0
    if n==1:
        return 0
    if n not in memo:
        memo[n] =min(cost[n-1]+dp(n-1),cost[n-2]+dp(n-2));
    return memo[n]
#memo는 안에 넣어도됨
def dpBottomUp(n):
    memo[0]=0;
    memo[1]=0;
    for i in range(2,n+1):
        memo[i] = min(cost[i-1]+memo[i-1],cost[i-2]+memo[i-2]);
    return memo[n];
print(dpBottomUp(5));