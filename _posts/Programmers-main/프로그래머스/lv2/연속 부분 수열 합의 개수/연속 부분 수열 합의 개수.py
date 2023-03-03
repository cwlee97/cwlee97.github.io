def solution(elements):
    answer = 0
    d_elements = elements + elements
    lis = []
    for i in range(len(elements)):
        for j in range(len(elements)):
            temp = sum(d_elements[i:i+j])
            lis.append(temp)
    lis.append(sum(elements))
    answer = len(set(lis))-1
    
    return answer