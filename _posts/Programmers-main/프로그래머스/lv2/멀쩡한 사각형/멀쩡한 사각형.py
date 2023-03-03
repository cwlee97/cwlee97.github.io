def solution(w,h):
    answer = w * h
    mod = []
    n = 0
    if h == 1 or w == 1:
        answer = 0
        return answer
    for i in range(1, h):
        if h * i / w % 1 == 0:
            n = i
            break
    for i in range(n):
        if h * (i + 1) / w % 1 == 0:
            mod.append(int(h * (i + 1) / w) - int(h * i / w))
        else:
            mod.append((int(h * (i + 1) / w) + 1) - int(h * i / w))
    x, y = divmod(w, n)
    if y == 0:
        answer -= sum(mod) * x
    else:
        answer -= sum(mod) * x + sum(mod[:y])
    return answer