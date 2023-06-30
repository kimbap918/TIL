def sol(nums):
    ans =False
    if nums==sorted(nums) or nums==sorted(nums,reverse=True) :
        ans=True
    return ans
print("Gnomes:")
for i in range(int(input())):
    nums=list(map(int,input().split()))
    if sol(nums)== True:
        print("Ordered")
    else :
        print("Unordered")