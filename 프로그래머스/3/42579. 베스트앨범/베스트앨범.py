def solution(genres, plays):
    answer = [];
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]][0] += plays[i];
            dic[genres[i]][1].append([plays[i],i]);
        else:
            dic[genres[i]] = [plays[i],[[plays[i],i]]];
    dic = sorted(dic.items(),key = lambda x: -x[1][0]);
    for item in dic:
        _,lis = item;
        numbers = sorted(lis[1],key = lambda x: -x[0]);
        if len(numbers)>=2:
            for number in numbers[:2]:
                answer.append(number[1]);
        else:
            answer.append(numbers[0][1])
    return answer