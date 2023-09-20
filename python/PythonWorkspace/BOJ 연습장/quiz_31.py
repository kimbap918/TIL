num = int(input()) # 변하지 않음, 초기 입력값
Num_first = num # num을 받아와서 
Num_new = -1 # 초기 입력시 0일 경우에 카운트가 올라가지 않고 바로 끝남.
cnt = 0

while num != int(Num_new): 
    B = str(Num_first)
    if Num_first < 10: # 입력받은 숫자가 10 보다 작으면 앞에 0을 붙임
        B = "0" + str(Num_first)  
    C = int(B[0]) + int(B[1])
    if C < 10:     
        C = str(C)
        C = "0" + C
    C = str(C)
    D = B[1]+C[1] # B의 뒷 자리와 C의 앞자리를 더해서 D에 저장
    Num_new = int(D) # Num_new = D
    Num_first = Num_new 
    cnt += 1
print(cnt)


