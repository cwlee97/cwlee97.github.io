def solution(board, moves):
    answer = 0
    collect = [0]
    for i in moves:
        temp = 0
        for j in range(len(board)):
            if board[j][i-1] != 0:
                temp = board[j][i-1]
                board[j][i-1] = 0
                if temp == collect[-1]:
                    answer += 2
                    del(collect[-1])
                else:
                    collect.append(temp)
                break
    return answer