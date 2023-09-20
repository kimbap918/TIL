T, C = map(int, input().split())
job = {}
result = []
for i in range(T):
    cant_hear = input()
    if cant_hear not in job:
        job[cant_hear] = 1
    else:
        job[cant_hear] += 1

for j in range(C):
    cant_see = input()
    if cant_see not in job:
        job[cant_see] = 1
    else:
        job[cant_see] += 1

for k, v in job.items():
    if v == 2:
       result.append(k)

print(len(result))
print("\n".join(sorted(result)))  
