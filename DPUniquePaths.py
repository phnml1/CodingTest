memo1 = {}
#내 풀이
def DPUniquePaths(m,n):
    if(n==1): return 1;
    if(m==1): return 1;
    if(m,n) not in memo1:
        memo1[(m,n)] =  DPUniquePaths(m-1,n)+DPUniquePaths(m,n-1);
    return memo1[(m,n)];
#강의 풀이 top-down
def uniquePaths(m,n):
    memo2 = [[-1]*n for _ in range(m)];
    def dfs(r,c):
        if r==0 and c == 0:
            memo2[r][c] = 1
            return memo2[r][c]
        unique_paths = 0
        if memo2[r][c] == -1:
            if r-1 >=0:
                unique_paths += dfs(r-1,c)
            if c-1>=0:
                unique_paths += dfs(r,c-1);
            memo2[r][c] = unique_paths;
        return memo2[r][c]
    return dfs(m-1,c-1);
#강의 풀이 bottom-up
def uniquePaths2(m,n):
    memo = [[-1]*n for _ in range(m)]
    
    for r in range(m):
        memo[r][0] = 1
    for c in range(n):
        memo[0][c] = 1
    for r in range(1,m):
        for c in range(1,n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1];
    return memo[m-1][n-1]
print(uniquePaths2(3,2));