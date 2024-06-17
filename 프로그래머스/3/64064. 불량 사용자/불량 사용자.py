
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
def combi(temp, number, calculate):
    global result
    if len(temp) == len(calculate):
        temp = set(temp)
        if temp not in result:
            result.append(temp)
        return
    else:
        for j in range(len(calculate[number])):
            if calculate[number][j] not in temp:
                temp.append(calculate[number][j])
                combi(temp, number+1, calculate)
                temp.pop()
result = []
def solution(user_id, banned_id):
    global result
    calculate = []
    for ban in banned_id:
        possible=[]
        for user in user_id:
            if len(ban) != len(user):
                continue
            else:
                count = 0
                for i in range(len(ban)):
                    if user[i] == ban[i]:
                        count+=1
                if count == len(ban)-ban.count('*'):
                    possible.append(user)
        calculate.append(possible)

    combi([], 0, calculate)
    return len(result)