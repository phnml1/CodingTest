def draw_stars(n):
  if n==1:
    return ['*']
  stars = draw_stars(n//3);
  L = []
  for i in stars:
    L.append(i * 3)
  for j in stars:
    L.append(j + ' '* (n//3) + j);
  for k in stars:
    L.append(k*3)
  
  return L

N = int(input())
print('\n'.join(draw_stars(N)));