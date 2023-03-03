def solution(N, stages):
  answer = []
  result = []
  for i in range(1, N + 1):
    play = 0
    clear = 0
    for j in stages:
      if i == j:
        play += 1
      if i <= j:
        clear += 1
    if clear != 0:
      result.append([play/clear, i])
    elif clear == 0:
      result.append([0, i])
  result = sorted(result, key = lambda x : (-x[0], x[1]))
  for x, y in result:
    answer.append(y)
  return answer