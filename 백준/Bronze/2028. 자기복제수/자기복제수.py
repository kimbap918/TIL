def 자기복제수(num):
    if str(num**2)[-len(str(num)):] == str(num):
        return "YES"
    return "NO"
for i in range(int(input())):
    print(자기복제수(int(input())))