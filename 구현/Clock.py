num = int(input())
count = 0
for h in range(num+1):
    for m in range(60):
        for s in range(60):
            clock = str(h) + str(m) + str(s);
            if '3' in clock:
                count += 1
print(count) 