months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
D, M = map(int, input().split())
print(days[(sum(months[:M-1]) + D) % 7])