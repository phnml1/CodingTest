n = int(input());
arr = []
for i in range(n):
  input_data = input().split();
  arr.append((input_data[0],int(input_data[1])));

def setting(data):
  return data[1];

arr = sorted(arr,key=setting);
# arr = sorted(arr,key=lambda student: student[1]);
print(arr);