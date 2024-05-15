from collections import defaultdict
def solution(participant, completion):
    dic = defaultdict(int);
    for i in participant:
        dic[i] += 1;
    for a in completion:
        dic[a] -= 1;
    for k in dic:
        if dic[k] > 0:
            return k
        