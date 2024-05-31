def solution(genres, plays):
    answer = [];
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]][0] += plays[i];
            dic[genres[i]][1].append([plays[i],i]);
        else:
            dic[genres[i]] = [plays[i],[[plays[i],i]]];
                              
    for (k,v) in sorted(dic.items(),key = lambda x: -x[1][0]):
        for number in sorted(v[1],key = lambda x: -x[0])[:2]:
            answer.append(number[1]);
                              
    return answer