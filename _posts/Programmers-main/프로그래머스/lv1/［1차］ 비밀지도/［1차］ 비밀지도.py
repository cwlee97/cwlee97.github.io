def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]
    count = 0

    for i in range(len(arr1)):
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]

    while count < n:
      while len(arr1[count]) < n:
        arr1[count] = '0' + arr1[count]
      while len(arr2[count]) < n:
        arr2[count] = '0' + arr2[count]
      count += 1
    
    for i in range(n):
      for j in range(n):
        if (arr1[i][j] == '0') and (arr2[i][j] == '0'):
          answer[i] += " "
        else:
          answer[i] += "#"
    return answer