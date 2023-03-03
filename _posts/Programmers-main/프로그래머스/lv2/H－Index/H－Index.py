def solution(citations):
    h = 0

    result = []
    
    while(True):
        count_down = 0
        count_up = 0
        for ele in citations:            
            if ele >= h:
                count_up += 1
            else:
                count_down += 1
                
        if (count_up >= h) and (count_down <= h):
            result.append(h)
            h += 1
        else:
            break

    answer = result[len(result)-1]
    return answer