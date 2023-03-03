def solution(n, k):
    answer = 0
    data = ''
    num_list = []
    dp = [2, 3]
    temp = ''
    while n > 0:
        n, mod = divmod(n, k)
        if mod == 0:     
            if temp != '':
                temp = int(temp)
                if temp in dp:
                    answer += 1
                elif temp == 1:
                        temp = ''
                else:
                    for i in range(2, int(temp**(1/2))+2):
                        if temp % i == 0:
                            break
                        elif i == int(temp**(1/2))+1:
                            answer += 1
                            dp.append(temp)
            temp = ''
        else:
            temp = str(mod) + temp
        if n == 0:
            if temp != '':
                  temp = int(temp)
                  if temp in dp:
                      answer += 1
                  elif temp == 1:
                      continue
                  else:
                      for i in range(2, int(temp**(1/2))+2):
                          if temp % i == 0:
                              break
                          elif i == int(temp**(1/2))+1:
                              answer += 1
                              dp.append(temp)
    return answer