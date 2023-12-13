strs = input();
strarr = [];
numarr = [];
result = '';
for a in strs:
  if a.isdecimal():
    numarr.append(int(a));
  else:
    strarr.append(a);
strarr.sort();
for a in strarr:
  result += a;
result += str(sum(numarr))
print(result)
