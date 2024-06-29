def solution(n, money):
    answer = 0
    dp = [[0 for _ in range(n+1)] for _ in range(len(money)+1)];
    for i in range(1,len(money)+1):
        dp[i][0] = 1;
    for i in range(1,len(money)+1):
        for j in range(1,n+1):
            if j < money[i-1]:
                dp[i][j] = dp[i-1][j] % 1000000007;
            else:
                dp[i][j] = (dp[i][j-money[i-1]] + dp[i-1][j]) % 1000000007;
    return dp[len(money)][n]