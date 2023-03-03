def solution(numbers, hand):
    answer = ''
    index = [[x, y] for x in range(4) for y in range(3)]
    for i in range(len(index)):
      print(i+1, ":", index[i])
    pos_l = [3, 0]
    pos_r = [3, 2]
    print(len(index))
    for i in range(len(numbers)):
        print("pos_l:", pos_l)
        print("pos_r:", pos_r)
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            pos_l = index[numbers[i]-1]
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            pos_r = index[numbers[i]-1]
        elif numbers[i] in [2, 5, 8, 0]:
            if numbers[i] == 0:
              numbers[i] = 11
            if abs(index[numbers[i]-1][0] - pos_l[0]) + abs(index[numbers[i]-1][1] - pos_l[1]) >\
              abs(index[numbers[i]-1][0] - pos_r[0]) + abs(index[numbers[i]-1][1] - pos_r[1]):
                answer += 'R'
                pos_r = index[numbers[i] - 1]
            elif abs(index[numbers[i]-1][0] - pos_l[0]) + abs(index[numbers[i]-1][1] - pos_l[1]) <\
              abs(index[numbers[i]-1][0] - pos_r[0]) + abs(index[numbers[i]-1][1] - pos_r[1]):
                answer += 'L'
                pos_l = index[numbers[i] - 1]
            else:
                if hand == "right":
                    answer += "R"
                    pos_r = index[numbers[i] - 1]
                else:
                  answer += 'L'
                  pos_l = index[numbers[i] - 1]
    return answer