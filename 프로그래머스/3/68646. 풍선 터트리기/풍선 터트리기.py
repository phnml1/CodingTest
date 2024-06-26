def solution(a):
    answer = 1;
    min_val = min(a);
    min_index = a.index(min_val);
    left,right = 0,len(a)-1;
    min_left,min_right = a[left],a[right];
    while left < min_index:
        if min_left >= a[left]:
            min_left = a[left];
            answer += 1;
        left += 1;
    while right > min_index:
        if min_right >= a[right]:
            min_right = a[right];
            answer += 1;
        right -= 1;
    return answer