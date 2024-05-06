import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())  # 기관차가 끌고 가던 객차의 수
    people = [0] + list(map(int, input().split()))
    M = int(input())  # 소형 기관차가 최대로 끌 수 있는 객차의 수

    # dp[1][n]: n번째 객차까지 1개의 소형 기관차를 사용했을 때 운송할 수 있는 최대 손님 수
    # dp[2][n]: n번째 객차까지 2개의 소형 기관차를 사용했을 때 운송할 수 있는 최대 손님 수
    # dp[3][n]: n번째 객차까지 3개의 소형 기관차를 사용했을 때 운송할 수 있는 최대 손님 수
    dp = [[0 for _ in range(N+1)] for _ in range(4)] 
    sums = 0 # 구간합

    # 최초 M개의 객차까지의 구간합을 구해놓는다.
    for i in range(1, M+1): 
        sums += people[i]
    dp[1][M] = sums # M번째 객차까지는 1개의 소형 기관차만 사용할 수 있다. 

    # 이제 M번째 이후의 객차부터 차례대로 살펴본다.
    for i in range(M+1, N+1):
        sums = sums - people[i-M] + people[i] # 구간합 갱신 
        dp[1][i] = max(dp[1][i-1], sums) # i번째 객차까지 1개의 소형 기관차를 사용했을 때 최댓값 갱신

        if i >= M*2: # 2개의 소형 기관차를 채울 수 있다면
            # i-1번째 객차까지 2개의 소형 기관차를 사용했을 때의 손님 수와
            # 현재 구간합에 i-M번째 객차까지 1개의 소형 기관차를 사용했을 때의 최대 손님수를 합한 수를 
            # 비교하여 큰 값으로 갱신
            dp[2][i] = max(dp[2][i-1], sums + dp[1][i-M]) 

        if i >= M*3: # 3개의 소형 기관차를 채울 수 있다면
            # i-1번째 객차까지 3개의 소형 기관차를 사용했을 때의 손님 수와
            # 현재 구간합에 i-M번째 객차까지 2개의 소형 기관차를 사용했을 때의 최대 손님수를 합한 수를 
            # 비교하여 큰 값으로 갱신
            dp[3][i] = max(dp[3][i-1], sums + dp[2][i-M])

    print(dp[3][N])
