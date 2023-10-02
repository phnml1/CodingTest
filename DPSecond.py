memo = {}
#Top Down
def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = cs(n-1) + cs(n-2);
    return memo[n];
#Bottm-top
def cs2(n):
    memo[1] = 1;
    memo[2] = 2;
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2];
    return memo[n];


print(cs2(5));