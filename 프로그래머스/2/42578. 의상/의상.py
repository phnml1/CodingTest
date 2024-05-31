def solution(clothes):
    dic = {};
    result = 1;
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]].append(cloth[0]);
        else:
            dic[cloth[1]] = [cloth[0]];
    print(dic)
    for key in dic:
        result *= len(dic[key])+1;
    return result-1;