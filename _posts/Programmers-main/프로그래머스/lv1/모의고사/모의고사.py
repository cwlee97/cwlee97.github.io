def solution(answers):
    count_1, count_2, count_3 = 0, 0, 0
    answer = []
    list1 = [(y % 5) + 1 for y in range(len(answers))]
    list2 = []
    list3 = []
    for i in range(len(answers)):
        if i % 2 == 0:list2.append(2)
        elif i % 8 == 1:list2.append(1)
        elif i % 8 == 3:list2.append(3)
        elif i % 8 == 5:list2.append(4)
        elif i % 8 == 7:list2.append(5)
    for i in range(len(answers)):
        if i % 10 <= 1:list3.append(3)
        elif i % 10 <= 3:list3.append(1)
        elif i % 10 <= 5:list3.append(2)
        elif i % 10 <= 7:list3.append(4)
        elif i % 10 <= 9:list3.append(5)
    
    for i in range(len(answers)):
        if answers[i] == list1[i]:
            count_1 += 1
        if answers[i] == list2[i]:
            count_2 += 1
        if answers[i] == list3[i]:
            count_3 += 1
    if max(count_1, count_2, count_3) == count_1:
        answer.append(1)
    if max(count_1, count_2, count_3) == count_2:
        answer.append(2)
    if max(count_1, count_2, count_3) == count_3:
        answer.append(3)
    return answer