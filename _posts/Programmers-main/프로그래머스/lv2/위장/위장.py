def solution(clothes):
    answer = 1
    kind_of_cloth = []
    for cloth in clothes:
        kind_of_cloth.append(cloth[1])
    cloth_dic = {x : 0 for x in kind_of_cloth}
    for cloth in clothes:
        for key in cloth_dic:
            if cloth[1] == key:
                cloth_dic[key] += 1
    for key in cloth_dic:
        answer *= (cloth_dic[key] + 1)
    answer -= 1
    return answer