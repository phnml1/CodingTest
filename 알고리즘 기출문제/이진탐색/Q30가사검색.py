# 내 코드
# def find_index(query,start,end):
#   if query[start] == '?':
#     while start<=end:
#       mid = (start + end)//2;
#       if query[mid] == '?':
#         start = mid + 1;
#       else:
#         end = mid - 1;
#     if query[mid] == '?':
#       return mid + 1
#     else:
#       return mid;
#   else:    
#     while start<=end:
#       mid = (start + end)//2;
#       if query[mid] == '?':
#         end = mid - 1;
#       else:
#         start = mid + 1;
#     if query[mid] == '?':
#       return mid;
#     else:
#       return mid+1;
# def solution(words, queries):
#     answer = []
#     for query in queries:
#       start = 0;
#       end = len(query) - 1;
#       search = ''
#       count = 0;
#       if query[start]=='?' and query[end] == '?':
#         for word in words:
#           if len(word) == len(query):
#             count+=1;
#       if query[start] == '?':
#         search = query[find_index(query,start,end):];
#         for word in words:
#           if len(word) == len(query):
#             for i in range(1,len(search)+1):
#               if word[-i] != search[-i]:
#                 break;
#               if i == len(search):
#                 count += 1;         
#       else:
#         search = query[:find_index(query,start,end)];
#         for word in words:
#           if len(word) == len(query):
#             for i in range(len(search)):
#               if word[i] != search[i]:
#                 break;
#               if i == len(search)-1:
#                 count+=1;
#       answer.append(count);
#     return answer
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a,left_value, right_value):
  right_index = bisect_right(a,right_value);
  left_index = bisect_left(a,left_value);
  return right_index - left_index;

array = [[] for _ in range (10001)];
reversed_array = [[] for _ in range(10001)];

def solution(words,queries):
  answer = []
  for word in words: #모든 단어를 접미사 와일드카드 배열 접두사 와일드카드 배열에 각각 삽입
    array[len(word)].append(word);
    reversed_array[len(word)].append(word[::-1]);
  
  for i in range(10001):
    array[i].sort();
    reversed_array[i].sort();
  
  for q in queries: #쿼리를 하나씩확인하며처리
    if q[0] != '?': #접미사에 와일드카드가 붙은경우
      res = count_by_range(array[len(q)], q.replace('?','a'),q.replace('?','z'));
    else:
      res = count_by_range(reversed_array[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
    answer.append(res)
  return answer
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "?????", "ka???", "pro?"]))