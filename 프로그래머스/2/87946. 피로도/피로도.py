from itertools import permutations;
def solution(k, dungeons):
    answer = -1
    indexes = [i for i in range(len(dungeons))];
    for case in list(permutations(indexes,len(indexes))):
        cur = k;
        count = 0;
        for i in list(case):
            min_fat, consume_fat = dungeons[i];
            if cur >= min_fat:
                cur -= consume_fat;
                count += 1;
            else:
                break;
        answer = max(answer, count)
    return answer