if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        num_dogs, food_per_dog, pound_per_food= map(float, input().split())
        total = num_dogs*food_per_dog*pound_per_food
        print('$%.2f' % total)