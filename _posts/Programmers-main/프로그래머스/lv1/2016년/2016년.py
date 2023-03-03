import datetime

def solution(a, b):
    date = datetime.datetime(2016, a, b)
    answer = date.strftime('%a').upper()
    return answer