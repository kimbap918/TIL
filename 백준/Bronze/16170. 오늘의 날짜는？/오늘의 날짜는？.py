import datetime
now = datetime.datetime.now() + datetime.timedelta(hours=9) #한국시간으로 나오니 수정해준다

print(now.year)
print(now.month)
print(now.day)