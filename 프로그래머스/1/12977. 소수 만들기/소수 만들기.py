from itertools import combinations
def solution(nums):
    answer = 0;
    for a in combinations(nums,3):
        number = sum(a);
        count = 0;
        for j in range(1,number//2+1):
            if number % j == 0:
                count += 1;
        if count == 1:
            answer += 1;
    return answer