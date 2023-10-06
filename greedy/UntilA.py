n,k = map(int, input().split())
count = 0
while True:
    if n==1:
        break
    if n%k ==0:
        n = n/k
    else:
        n = n-1
    count += 1
print(count);

#책풀이
# n,k = map(int, input().split)
# result = 0
# while n>=k:
#     while n%k !=0:
#         n-=1
#         result+=1
#     n//=k
#     result += 1
# while n>1:
#     n-=1
#     result +=1
# print(result)