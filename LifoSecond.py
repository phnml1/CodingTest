def dailyTemputures(temp):
    # temp의 length만큼 배열선언
    ans = [0] * len(temp);
    stack = []
    # enumerate 배열은 인덱스와 값을 모두 반환
    for cur_day, cur_temp in enumerate(temp):
        while stack and stack[-1][1] < cur_temp:
            #_는 필요없으므로 _로처리
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans

dailyTemputures([73,71,75,71,69,72,76,73])