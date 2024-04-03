# learn_words = ['a','n','t','i','c'];
# n,k = map(int,input().split());
# words = [];
# cases = []
# result = 0;
# for _ in range(n):
#   cur = input().rstrip()[4:-4];
#   words.append(cur);
#   for i in cur:
#     if i not in learn_words and i not in cases:
#       cases.append(i);
# def compare(learn,start):
#   global result;
#   if len(learn) == k:
#     count = 0;
#     for word in words:
#       for i in range(len(word)):
#         if word[i] not in learn:
#           break;
#         if i == len(word)-1:
#           count += 1;
#     result = max(count,result);
#   else:
#     for i in range(start,len(cases)):
#       if cases[i] not in learn:
#         learn.append(cases[i]);
#         compare(learn,i+1);
#         learn.pop();
# if k<len(learn_words):
#   print(0);
# else:
#   compare(learn_words,0);
#   print(result);
from itertools import combinations 
import sys
n, k = map(int, input().split())
answer = 0
# a,n,t,i,c는 반드시 가르쳐야 함

first_word = {'a','n','t','i','c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word
data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

def countReadableWords(data, learned):
   cnt = 0
   for word in data:
      canRead = 1
      for w in word:
          # 안배웠으니까 못읽는다.
         if learned[ord(w)] == 0:
            canRead = 0
            break
      if canRead == 1:
         cnt += 1
   return cnt

if k >= 5:
   learned = [0] * 123
   for x in first_word:
      learned[ord(x)] = 1

   # 남은 알파벳 중에서 k-5개를 선택해본다.
   for teach in list(combinations(remain_alphabet, k-5)):
      for t in teach:
         learned[ord(t)] = 1
      cnt = countReadableWords(data, learned)

      if cnt > answer:
         answer = cnt
      for t in teach:
         learned[ord(t)] = 0
   print(answer)
else:
   print(0)
 


# import sys

# input = sys.stdin.readline

# def dfs(start, cnt):
#   global ans;
#   if cnt == k-5:
#     tmp = 0;
#     for word in words:
#       is_contain = True;
#       for c in word:
#         if not check[ord[c] - ord['a']]:
#           is_contain = False
#           break;
#       if is_contain:
#         tmp += 1;
#     ans = max(ans,tmp);
#     return
#   for i in range(start,26):
#     if not check[i]:
#       check[i] = True;
#       dfs(i,cnt+1);
#       check[i] = False;
# n, k = map(int, input().split())

# # set을 활용하여 중복을 제거함으로써 해당 단어를 읽는데 필요한 최소한의 글자를 구함
# words = [set(input().rstrip()) for _ in range(n)]
# check = [False] * 26
# ans = 0

# # 가르칠 글자의 수가 5(a, n, t, i, c)보다 작은 경우
# if k < 5:
#   print(0)    # 읽을 수 있는 단어가 없음
#   exit(0)
# # 가르칠 글자의 수가 26(a, b, c, ..., z)인 경우
# elif k == 26:
#   print(n)    # 모든 단어를 읽을 수 있음
#   exit(0)

# # a, c, i, n, t 는 무조건 배워야 함
# for c in ('a', 'c', 'i', 'n', 't'):
#   check[ord(c) - ord('a')] = True

# dfs(0, 0)
# print(ans)