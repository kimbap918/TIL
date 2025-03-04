import sys

input = sys.stdin.readline

def cal(N, locations):
    x0, y0, E0 = locations[0]
    wifi = [max(0, E0 - (abs(x0 - x) + abs(y0 - y))) for x, y, _ in locations[1:]]
    hotspot = [0] * N

    for i in range(1, N+1):
        xi, yi, Ei = locations[i]
        if Ei > 0: # 핫스팟이 존재하는 경우
            for j in range(N):
                xj, yj, _ = locations[j+1]
                hotspot[j] += max(0, Ei - (abs(xi - xj) + abs(yi - yj)))

    max_speed = -1
    for i in range(N):
        speed = wifi[i] - hotspot[i]
        if speed > 0:
            max_speed = max(max_speed, speed)

    return max_speed if max_speed != -1 else "IMPOSSIBLE"


N = int(input())
locations = []

for i in range(N+1):
    x, y, E = map(int, input().split())
    locations.append((x, y, E))

print(cal(N, locations))

