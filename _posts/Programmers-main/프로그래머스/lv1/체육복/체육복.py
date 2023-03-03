def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    del_list = []
    students = [x for x in range(1, n+1)]
    
    for student in lost:
        students.remove(student)
    for l_student in lost:
        if l_student in reserve:
            reserve.remove(l_student)
            students.append(l_student)
            del_list.append(l_student)
    for student in del_list:
        lost.remove(student)
        
    for l_student in lost:
        if l_student - 1 in reserve:
            reserve.remove(l_student - 1)
            students.append(l_student)
        elif l_student + 1 in reserve:
            reserve.remove(l_student + 1)
            students.append(l_student)
    
    students = list(set(students))
    answer = len(students)
    return answer