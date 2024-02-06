tc = int(input())

for i in range(1, tc + 1) :
  gan = list(map(int, input().split()))
  sau = list(map(int, input().split()))

  gan_score = gan[0] + gan[1]*2 + gan[2]*3 + gan[3]*3 + gan[4]*4 + gan[5]*10
  sau_score = sau[0] + sau[1]*2 + sau[2]*2 + sau[3]*2 + sau[4]*3 + sau[5]*5 + sau[6]*10

  if gan_score > sau_score :
    print(f"Battle {i}: Good triumphs over Evil")
  elif gan_score < sau_score :
    print(f"Battle {i}: Evil eradicates all trace of Good")
  else :
    print(f"Battle {i}: No victor on this battle field")