def solution(participant, completion):
    answer = ''
    name_dict = {}
    for name in participant:
        if name in name_dict:
            name_dict[name]+=1
        else:
            name_dict[name]=1
    for i in completion:
        name_dict[i]-=1
    for key, value in name_dict.items():
        if value==1:
            answer = key
    return answer