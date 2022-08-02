N = int(input())
chat_list = {}
cnt = 0

for i in range(N):
    chat = input()
    if chat == "ENTER":
        for k, v in chat_list.items():
            if v == 1:
                cnt += 1
        chat_list = {}

    elif chat != "ENTER":
        if chat not in chat_list:
            chat_list[chat] = 1

for k, v in chat_list.items():
    if v == 1:
        cnt += 1

print(cnt)