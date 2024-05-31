from itertools import permutations
def solution(numbers):
    indexs_arr = []
    answer = []
    for i in range(len(numbers)):
        indexs_arr.append(i);
    for i in range(1,len(numbers)+1):
        for case in list(permutations(indexs_arr,i)):
            isPrime = True;
            cur = '';
            for j in list(case):
                cur += numbers[j];
            cur_num = int(cur);
            for k in range(2, int(cur_num**0.5)+1):
                if cur_num % k == 0:
                    isPrime = False;
            if isPrime and cur_num>1:
                answer.append(cur_num);       
    return len(set(answer));