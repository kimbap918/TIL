chicken = int(input())
coke, beer = map(int, input().split())
eat = coke//2 + beer

if chicken >= eat :
    print(eat)
else :
    print(chicken)