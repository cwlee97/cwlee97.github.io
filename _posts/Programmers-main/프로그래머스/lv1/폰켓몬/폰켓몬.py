def solution(nums):
    answer = 0
    choose = int(len(nums) // 2)
    nums = list(set(nums))
    
    if choose > len(nums):
        answer = len(nums)
    else:
        answer = choose
    return answer