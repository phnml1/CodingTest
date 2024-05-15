def solution(phone_book):
    hash_map = {};
    for number in phone_book:
        hash_map[number] = 1;
    for number in phone_book:
        temp = ''
        for i in number:
            temp += i;
            if temp in hash_map and temp != number:
                return False;
        
    return True