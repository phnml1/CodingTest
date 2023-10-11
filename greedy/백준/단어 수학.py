Max_Number = 9;
alphabet = {};
arr = []
result = 0
n = int(input());
for i in range(n):
    arr.append(list(map(str,input())));
arr.sort(key=len,reverse=True)
while len(arr[0])>0:
    if arr[0][0] not in alphabet:
        cur_alphabet= arr[0].pop(0);
        alphabet[cur_alphabet] = 10 ** len(arr[0])
    else:
        alphabet[arr[0].pop(0)] += 10**len(arr[0]);
    arr.sort(key=len,reverse=True)
sum_values = alphabet.values();
sum_list = list(sum_values);
sum_list.sort(reverse=True);
for value in sum_list:
    result += value*Max_Number;
    Max_Number-=1;
print(result)