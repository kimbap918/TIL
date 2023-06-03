import sys
input = sys.stdin.readline

N = int(input())
student = list(map(int, input().split()))
ttl, sub = map(int, input().split())
cnt = N

for i in student:
    i -= ttl # 총감독관을 뺀다
    if i > 0: # 총감독관 감독 수를 뺀 뒤 0 보다 학생 수가 많다면
        if i % sub: # 보조감독관으로 나눠서 나머지가 생긴다면
            cnt += (i // sub)+1
        else:
            cnt += (i // sub)

print(cnt)
