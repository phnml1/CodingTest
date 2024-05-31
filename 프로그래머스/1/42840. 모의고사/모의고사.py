def solution(answers):
    result = [0,0,0]
    answer = []
    orders = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] ==orders[j][i%len(orders[j])]:
                result[j] += 1;
    for i in range(3):
        if max(result) == result[i]:
            answer.append(i+1);
    return answer