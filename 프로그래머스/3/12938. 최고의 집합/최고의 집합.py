def solution(n, s):
    answer = []
    remain,share = s % n, s//n;
    if n>s:
        return [-1];
    if remain == 0:
        return [share]*n;
    else:
        for i in range(remain):
            answer.append(share + 1);
        answer.extend([share] * (n- remain));
        return sorted(answer);