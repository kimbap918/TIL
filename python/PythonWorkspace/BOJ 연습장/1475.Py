from collections import Counter
import math
# 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 
# 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오
num_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cnt = 1

N = input()
counter = Counter(N)
count_6_9 = counter.get('6', 0) +  counter.get('9', 0)
counter['6'] = counter['9'] = math.ceil(count_6_9 / 2)


print(max(counter.values()))
