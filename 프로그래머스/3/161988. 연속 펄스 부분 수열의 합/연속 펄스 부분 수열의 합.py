def solution(sequence):
    sequence = [ (-1) ** (idx+1) * sequence[idx] for idx in range(len(sequence)) ]
    min_val, max_val = sequence[0], sequence[0];
    dp = [[sequence[0],sequence[0]] for _ in range(len(sequence))];
    for i in range(1,len(sequence)):
        dp[i][0] = min(dp[i-1][0] + sequence[i], sequence[i]);
        dp[i][1] = max(dp[i-1][1] + sequence[i], sequence[i]);
    min_val = min(map(min, dp));
    max_val = max(map(max, dp));
    return max(abs(min_val),abs(max_val));
    