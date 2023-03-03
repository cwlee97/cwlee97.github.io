from itertools import combinations

def solution(nums):
    answer = -1
    del_list = []
    data = list(combinations(nums, 3))
    for i in range(len(data)):
        summary = sum(data[i])
        if summary == 2:
            continue
        for j in range(2, summary//2+1):
            if summary % j == 0:
                del_list.append(i)
                break
    del_list.sort(reverse = True)
    for i in del_list:
        del(data[i])
        
    answer = len(data)
    return answer