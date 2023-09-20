def counting_stars(n):
  if n == 1: # 별 찍기
    return ['*']

  stars = counting_stars(n//3) # 3의 거듭제곱 값들을 나눈 몫을 함수로 호출
  L = []

  for star in stars:
    L.append(star*3)
  for star in stars:
    L.append(star+' '*(n//3)+star)
  for star in stars:
    L.append(star*3)

  return L

N = int(input())
print('\n'.join(counting_stars(N)))