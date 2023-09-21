w = int(input())
l = int(input())
h = int(input())
print(["bad", "good"][min(w, l) / h >= 2 and max(w, l) / min(w, l) <= 2])