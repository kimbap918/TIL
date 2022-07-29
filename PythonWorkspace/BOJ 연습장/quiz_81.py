N = int(input())
j = 1

seller_dict = {}
seller_list = []
for i in range(N):
    book = input()
    seller_list.append(book)

for best in seller_list:
    seller_dict[best] = 0

for best_seller in seller_list:
    seller_dict[best_seller] += 1

result = sorted(seller_dict.keys(), reverse= False)

print(max(result, key=seller_dict.get))
