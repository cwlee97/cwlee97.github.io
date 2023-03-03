import heapq

def solution(scoville, K):
    answer = 0
    new_sco = 0
    heapq.heapify(scoville)
    for i in range(len(scoville) - 1):
        if scoville[0] < K:
            new_sco = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            if len(scoville) == 0:
                if new_sco < K:
                    answer = -1
                    break
            heapq.heappush(scoville, new_sco)
            answer += 1
        else:
            break
    
    return answer