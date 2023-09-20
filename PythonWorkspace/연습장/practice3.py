# 풀이를 참고했습니다.
ans = list(map(int, input()))
goorm = list(map(int, input()))
cnt = 0

# 입력 값이  ans에 들어있지 않을 경우(fail)
def fail():
	for i in range(4):
		if res[i] != -1:
			continue
        while True:
            temp = (goorm[i] + 1) % 10
            out = temp not in goorm
            goorm[i] = temp
            if out:
                break

# 입력 값은 들어있지만 위치가 같지 않을때
def ball():
	if 1 not in res:
		return
	pos = []
	value = []
	for i in range(4):
		# 스트라이크가 아니면
		if res[i] != 0:
			# 인덱스와 해당 입력값 추가
			pos.append(i)
			value.append(goorm[i])
	for i in range(len(pos)):
		# 스트라이크면
		if i == 0:
			# 해당 위치에 값의 맨 끝값을 저장
			goorm[pos[i]] = value[-1]
		else:
			# 해당 위치에 값을 오른쪽으로 한칸 옮김
			goorm[pos[i]] = value[i-1]


while True:
	cnt += 1
	res = [-1 for i in range(4)]
	if ans == goorm:
		print(cnt)
		break
	
	for i in range(4):
		# 값이 들어있는 경우
		if goorm[i] in ans:
			# 값과 위치가 완전히 같다면(strike)
			if goorm[i] == ans[i]:
				res[i] = 0
			# 값은 들어있지만 위치가 같지 않을때(ball)
			else:
				res[i] = 1

	fail()
	ball()
		