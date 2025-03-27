import sys
input = sys.stdin.readline;
st1 = list(input().rstrip());
num = int(input());
st2 = [];
for _ in range(num):
    arr = input().split();
    if arr[0] == 'L' and st1:
        st2.append(st1.pop());
    if arr[0] == 'D' and st2:
        a = st2.pop();
        st1.append(a);
    if arr[0] == 'B' and st1:
        st1.pop();
    if arr[0] == 'P':
        st1.append(arr[1]);
answer = st1 + st2[::-1];
print(''.join(answer));