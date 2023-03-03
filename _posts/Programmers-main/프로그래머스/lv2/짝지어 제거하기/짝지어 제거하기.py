from collections import deque

def solution(s):
  s = deque(s)
  data = deque()
  while len(s) > 0:
    if len(data) != 0:
      if s[0] == data[-1]:
        s.popleft()
        data.pop()
        continue
    data.append(s.popleft())

  if len(data) == 0:
    answer = 1
  else:
    answer = 0
  return answer