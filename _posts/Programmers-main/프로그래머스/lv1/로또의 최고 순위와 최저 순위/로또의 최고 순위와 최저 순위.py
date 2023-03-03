def solution(lottos, win_nums):
  answer = []
  count = 0

  lottos = sorted(lottos)
  win_nums = sorted(win_nums)
  zeros = lottos.count(0)
  for i in lottos:
    if i in win_nums:
      count += 1
  answer = [7 - (zeros + count), 7 - count]
  for i in range(len(answer)):
    if answer[i] >= 6:
      answer[i] = 6
  return answer