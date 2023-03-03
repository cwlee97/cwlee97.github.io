def solution(n, costs):
  answer = 0
  weights = []
  nodes = []
  visited = []

  for i in range(len(costs)):
    weights.append(costs[i][2])
    nodes.append([costs[i][0], costs[i][1]])
  for i in range(len(costs)):
      if weights[i] == min(weights):
        answer += weights[i]
        visited.append(nodes[i][0])
        visited.append(nodes[i][1])
        break
  for i in range(len(costs)):
    if nodes[i][0] in visited:
      nodes[i][0] = "pass"
    if nodes[i][1] in visited:
      nodes[i][1] = "pass"
  while [["pass", "pass"]] * len(nodes) != nodes:
    temp = []
    temp_weight = []
    temp_pos = []
    temp_num = 0
    for i in range(len(nodes)):
      if nodes[i].count("pass") == 1:
        temp_weight.append(weights[i])
        temp_pos.append(i)
  
    for i in range(len(temp_weight)):
      if temp_weight[i] == min(temp_weight):
        answer += temp_weight[i]
        temp = nodes[temp_pos[i]].copy()
        temp.remove("pass")
        temp_num = temp[0]
        break
    for i in range(len(nodes)):
      if nodes[i][0] == temp_num:
        nodes[i][0] = "pass"
      elif nodes[i][1] == temp_num:
        nodes[i][1] = "pass"
  return answer