import heapq

def solution(N, road, K):
    answer = []
    graph = [[]for _ in range(N + 1)]
    for i in range(len(road)):
        graph[road[i][0]].append([road[i][1], road[i][2]])
        graph[road[i][1]].append([road[i][0], road[i][2]])
        
    start = 1
    table = [500001] * (N + 1)
    table[start] = 0
    
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        Node, Weight = heapq.heappop(q)
        
        if table[Node] < Weight:
            continue
        for n, w in graph[Node]:
            if Weight + w < table[n]:
                table[n] = Weight + w
                heapq.heappush(q, (n, table[n]))
    for i in range(1, len(table)):
        if table[i] <= K:
            answer.append(i)
    answer = len(answer)
    return answer