def solution(maps):
    answer = 1
    n, m = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = []
    queue.append((0, 0))
    while queue:
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                if nx + 1 == n and ny + 1 == m:
                    answer += 1
                    return answer
                queue.append((nx, ny))
        answer += 1
    answer = -1
    return answer