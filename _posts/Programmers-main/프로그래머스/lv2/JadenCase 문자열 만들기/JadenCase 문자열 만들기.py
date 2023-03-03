def solution(s):
  answer = ""
  count = 0
  temp = ""
  while count < len(s):
    if s[count] == " ":
        answer += temp.capitalize()
        temp = ""
        answer += " "
    else:
      temp += s[count]
    count += 1
    if count == len(s):
      answer += temp.capitalize()
  return answer