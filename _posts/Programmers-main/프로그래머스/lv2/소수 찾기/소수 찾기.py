def generate(numbers, r, chosen, visited, num_list):
    num = ""
    if len(chosen) == r:
        for i in chosen:
            num += i
        num_list.append(num)
        
    
    for i in range(len(numbers)):
        if not visited[i]:
            chosen.append(numbers[i])
            visited[i] = True
            generate(numbers, r, chosen, visited, num_list)
            visited[i] = False 
            chosen.pop()
    return
    
            
def solution(numbers):
    visited = [False] * len(numbers)
    num_list = []
    del_list = []
    chosen = []
    for i in range(1, len(numbers)+1):
        generate(numbers, i, chosen, visited, num_list)
    num_list = list(set(map(int, num_list)))
    for i in [0, 1]:
        if i in num_list:
            num_list.remove(i)
    for num in num_list:
        if num == 2:
            continue
        else:
            for i in range(2, num):
                if num % i == 0:
                    del_list.append(num)
                    break
    for num in del_list:
        num_list.remove(num)
    answer = len(num_list)
    return answer