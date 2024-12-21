# 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

mo = "aeiou"
ja = "bcdfghjklmnpqrstvwxyz"
allowed = {"oo", "ee"}

while True:
    word = input()
    if word == "end":
        break

    mo_flag = any(w in mo for w in word)  # 모음 포함 여부
    mo_cnt = ja_cnt = 0
    flag = True

    for i, w in enumerate(word):
        # 모음/자음 카운팅
        if w in mo:
            mo_cnt += 1
            ja_cnt = 0
        elif w in ja:
            ja_cnt += 1
            mo_cnt = 0
        else:
            mo_cnt = ja_cnt = 0

        if mo_cnt >= 3 or ja_cnt >= 3:  # 연속 조건 위반
            flag = False
            break

        # 같은 글자 연속 검사
        if i > 0 and word[i] == word[i - 1] and word[i - 1:i + 1] not in allowed:
            flag = False
            break

    if not mo_flag:  # 모음 포함 조건
        flag = False

    if flag:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
