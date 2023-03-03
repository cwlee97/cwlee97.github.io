def solution(new_id):
    answer = ''
    del_list = []
    new_id = new_id.lower()
    validation = []
    for i in range(ord('a'), ord('z') + 1):
        validation.append(i)
    for i in range(ord('0'), ord('9') + 1):
        validation.append(i)
    for i in [ord('-'), ord('_'), ord('.')]:
        validation.append(i)
    for i in range(len(new_id)):
        if ord(new_id[i]) not in validation:
            del_list.append(new_id[i])
    for i in del_list:
      new_id = new_id.replace(i, "")

    while ".." in new_id:
      new_id = new_id.replace("..", ".")

    new_id = new_id.strip(".")

    if new_id == "":
      new_id = "a"
    
    if len(new_id) >= 16:
      new_id = new_id[:15]
      new_id = new_id.strip(".")
    
    while len(new_id) < 3:
      new_id += new_id[-1]

    return new_id