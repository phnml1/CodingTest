def solution(s):
    answer = 1;
    for i in range(1,len(s)-1):
        left = i-1;
        right = i+1;
        count = 1;
        while  0<=left and right<len(s) and s[left] == s[right]:
            count += 2;
            left -= 1;
            right += 1;
        answer = max(count,answer);
    for i in range(len(s)-1):
        left = i;
        right = i+1;
        count = 0;
        while  0<=left and right<len(s) and s[left] == s[right]:
            count += 2;
            left -= 1;
            right += 1;
        answer = max(count,answer);
    return answer