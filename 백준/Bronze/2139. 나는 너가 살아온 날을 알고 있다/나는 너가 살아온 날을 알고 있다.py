from datetime import date
def numOfDays(date1, date2):
    return (date2 - date1).days
while 1:
    d,m,y=map(int, input().split())
    if d==0 and m==0 and y==0 :break
    date1 = date(y, 1, 1)
    date2 = date(y, m, d)
    print(numOfDays(date1, date2)+1)