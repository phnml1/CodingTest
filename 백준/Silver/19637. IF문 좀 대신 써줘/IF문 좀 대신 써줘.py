import sys
from collections import defaultdict
input = sys.stdin.readline;
dict = defaultdict();
n,m = map(int,input().split());
for _ in range(n):
    st, number = input().split();
    number = int(number);
    if number not in dict:
        dict[number] = st;
arr = list(dict.keys());
for _ in range(m):
    cur = int(input());
    left = 0;
    right = len(arr)-1;
    result = ''
    while left <= right:
        mid = (left + right)//2;
        if cur < arr[mid]:
            result = dict[arr[mid]];
            right = mid-1;
        elif cur == arr[mid]:
            result = dict[arr[mid]];
            break;
        else:
            left = mid+1;
    print(result);

    