# 내풀이
# def MaxNumber(arr,k,m):
#     max1=0;
#     max2=0;
#     answer=0;
#     count=0;
#     for num in arr:
#         max1 = max(num,max1);
#     arr.remove(max1);
#     for num in arr:
#         max2 = max(num,max2);
#     for _ in range(m):
#         if count<k:
#             count += 1;
#             answer += max1;
#         elif count == k:
#             count = 0
#             answer += max2;
#     return answer;

# print(MaxNumber([2,4,5,4,6],3,8))

#책풀이 1
# N,M,k를 공백으로 구분하여 입력받기
# n,m,k = map(int,input().split())
# data = list(map(int,input().split()))

# data.sort() #입력받은 수 정렬
# first = data[n-1] #가장 큰 수
# second = data[n-2] #두번째로 큰 수

# result = 0
# while True:
#     for i in range(k):
#         if m==0:
#             break
#         result += first
#         m -= 1
#     if m==0:
#         break
#     result += second
#     m-=1
# print(result);

n,m,k = map(int, input().split)
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
# 가장큰수는 수열의 길이인 k+1을 나누고 k를 곱한값 + 나머지가됨
count = int(m/ (k+1)) *k
count += m%(k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)