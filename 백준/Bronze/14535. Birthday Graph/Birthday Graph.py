import sys
input = sys.stdin.readline

cnt = 1

while True:
    month = {"Jan":0, "Feb":0, "Mar":0, "Apr":0, "May":0, "Jun":0, "Jul":0, "Aug":0, "Sep":0, "Oct":0, "Nov":0, "Dec":0}
    num = int(input())
    if num == 0:
        break
    else:
        for _ in range(num):
            birth = input().split()
            if birth[1] == "01":
                month["Jan"] += 1
            elif birth[1] == "02":
                month["Feb"] += 1
            elif birth[1] == "03":
                month["Mar"] += 1
            elif birth[1] == "04":
                month["Apr"] += 1
            elif birth[1] == "05":
                month["May"] += 1
            elif birth[1] == "06":
                month["Jun"] += 1
            elif birth[1] == "07":
                month["Jul"] += 1
            elif birth[1] == "08":
                month["Aug"] += 1
            elif birth[1] == "09":
                month["Sep"] += 1
            elif birth[1] == "10":
                month["Oct"] += 1
            elif birth[1] == "11":
                month["Nov"] += 1
            else:
                month["Dec"] += 1

        print("Case #"+str(cnt)+":")

        for key, value in month.items():
            print(key+":"+"*"*value)
    cnt +=1