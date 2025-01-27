def has_33(nums):
    l = len(nums)
    count = 0
    for i in range(1, l):
        if nums[i-1] == 3 and nums[i] == 3:
            count+=1
        
    if count != 0 :
        return True
    else:
        return False


a = list(map(int, input().split()))

print(has_33(a))