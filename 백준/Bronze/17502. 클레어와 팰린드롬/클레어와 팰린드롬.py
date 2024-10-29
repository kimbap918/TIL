N = int(input())
palindrome = list(input())

for i in range(N):
    if palindrome[i].isalpha():
        palindrome[-i - 1] = palindrome[i]

for i in range(N):
    if palindrome[i] == "?":
        palindrome[i] = "a"

print("".join(palindrome))
