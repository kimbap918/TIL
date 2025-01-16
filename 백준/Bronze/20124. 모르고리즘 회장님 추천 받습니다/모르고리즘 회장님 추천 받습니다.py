n=int(input())
nums=[]
for i in range(n):
    name, score = input().split()
    nums.append([name,int(score)])
nums.sort(key=lambda x: (-x[1],x[0]))
print(nums[0][0])