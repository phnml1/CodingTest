import sys;
input = sys.stdin.readline;

result = 1e9;
st = input().rstrip();
length = len(st);
a_count = st.count('a');
st = st + st;
for i in range(length):
  result = min(result,st[i:i+a_count].count('b'));
print(result)