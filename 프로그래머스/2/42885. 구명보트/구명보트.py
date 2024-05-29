def solution(people, limit):
    people.sort();
    start, end = 0, len(people) - 1;
    answer, passengers = 0,0;
    
    while start < end:
        cur_weight = people[start] + people[end];
        if cur_weight<=limit:
            passengers += 2;
            answer += 1;
            start += 1;
            end -= 1;
        else:
            end -= 1;
    answer += (len(people) - passengers);
    return answer