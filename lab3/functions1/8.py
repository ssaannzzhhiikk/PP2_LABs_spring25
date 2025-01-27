def spy_game(nums):
    t = False
    for i in range(2,len(nums)):
        if nums[i-2] == 0 and nums[i-1] == 0 and nums[i] == 7:
            t = True

    return t


a = list(map(int, input().split()))
print(spy_game(a)) 
