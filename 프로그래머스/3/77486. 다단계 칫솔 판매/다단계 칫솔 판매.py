from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []
    persons = defaultdict(str);
    sells = defaultdict(lambda: 0);
    for i in range(len(referral)):
        persons[enroll[i]] = referral[i];
    for i in range(len(seller)):
        interest = amount[i]*100//10;
        sells[seller[i]] +=  amount[i]*100 - interest;
        cur = persons[seller[i]];
        while cur != '-':
            if interest == 0:
                break;
            sells[cur] += interest - interest//10;
            cur = persons[cur];
            interest = interest // 10;
    for member in enroll:
        answer.append(sells[member]);
    return answer