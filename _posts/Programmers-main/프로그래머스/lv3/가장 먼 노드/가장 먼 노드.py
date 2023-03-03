import heapq

def solution(n, edge):
    answer = 0
    inf = int(1e9)
    graph = [[] for _ in range(n + 1)]
    
    for i in range(len(edge)):
        graph[edge[i][0]].append((edge[i][1], 1))
        graph[edge[i][1]].append((edge[i][0], 1))
    
    for i in range(1, n+1):
        graph[i].sort()
        
    start = 1
    table = [inf] * (n + 1)
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
    table[0] = 0
    for i in table:
        if i == max(table):
            answer += 1
    return answer