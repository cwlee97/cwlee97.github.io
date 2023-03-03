def solution(id_list, report, k):
  report = list(set(report))
  answer_dic = {x:0 for x in id_list}
  id_dic = {x:0 for x in id_list}
  ban = []
  for i in range(len(report)):
        report[i] = list(map(str, report[i].split(" ")))

  for i in range(len(report)):
    id_dic[report[i][1]] += 1
  for i in id_dic:
    if id_dic[i] >= k:
      ban.append(i)
  
  for i in range(len(report)):
    if report[i][1] in ban:
      answer_dic[report[i][0]] += 1
  answer = list(answer_dic.values())

  return answer