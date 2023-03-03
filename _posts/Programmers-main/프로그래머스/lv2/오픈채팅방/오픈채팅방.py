def solution(record):
    answer = []
    for i in range(len(record)):
        record[i] = list(map(str, record[i].split(" ")))
    user_dic = {x[1]:"" for x in record}
    for i in record:
      if len(i) == 3:
        user_dic[i[1]] = i[2]

    for i in record:
      if i[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(user_dic[i[1]]))

      elif i[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(user_dic[i[1]]))
    return answer