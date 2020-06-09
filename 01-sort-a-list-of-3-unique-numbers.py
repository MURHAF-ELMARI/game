def sortNums(nums):
    Max = max(nums)
    a = [0] * (Max+1)

    for i in nums:
        a[i]+=1
    j = 0
    i = 0
    while i < len(a):

        while (a[i] > 0):
            nums[j] = i
            a[i]-=1
            j += 1
        i+=1
    return nums


print(sortNums([5, 4, 6, 5, 6]))
