num = int(input());
count = 9999;
for i in range(num//5+1):
    if (num-(5*i))%3==0:
        count = min(count,i+(num-(5*i))/3);
if(count==9999):
    print(-1);
else:
    print(int(count));
    