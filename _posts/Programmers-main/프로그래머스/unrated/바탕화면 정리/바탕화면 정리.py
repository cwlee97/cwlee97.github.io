def solution(wallpaper):
    answer = []
    bool_f = False
    x_min, x_max = 51, 0
    y_min, y_max = 51, 0
    for idx in range(len(wallpaper)):
        if '#' in wallpaper[idx]:
            if bool_f == False:
                y_min = idx
                bool_f = True
            r_tmp = wallpaper[idx].find('#')
            l_tmp = wallpaper[idx].rfind('#')
            if r_tmp < x_min: x_min = r_tmp
            if l_tmp > x_max: x_max = l_tmp
            y_max = idx
    answer = [y_min, x_min, y_max + 1, x_max + 1]
    return answer