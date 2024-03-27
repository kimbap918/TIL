nums = []
for i in range(3):
    a, b = map(int, input().split())
    if a * 10 >= 5000:
        a = a * 10 - 500
    else:
        a *= 10
    b *= 10
    nums.append(b / a)
if max(nums) == nums[0]:
    print('S')
elif max(nums) == nums[1]:
    print('N')
else:
    print('U')