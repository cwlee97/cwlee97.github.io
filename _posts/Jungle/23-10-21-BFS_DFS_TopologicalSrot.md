---
layout: single
title: BFS & DFS & Topological Sorting
categories: Jungle
---

## BFS, DFS
두 가지 모두 그래프 탐색의 기법으로, 여기서 그래프 탐색이란, 하나의 정점에서부터 시작하여 차례대로 모든 정정을 한 번씩 방문하는 것을 말함

## 너비 우선 탐색(BFS, Breadth-First Search)
* 루트 노드(또는 다른 임의의 노드)에서 시작하여 인접한 노드를 먼저 탐색하는 방법
    * 시작 정점으로부터 가까운 정점을 먼저 방문하고, 먼 정점을 나중에 방문
    * 깊게 탐색하기 전에 넓게 탐색하는 법

### 특징
* 재귀적으로 동작하지 않음
* 어떤 노드를 방문했는지 저장할 배열이 필요
* FIFO 원칙의 자료구조인 큐를 사용

### 구현
```python
def bfs(graph, root):
    visited = list()
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for next_node in graph[node]:
                queue.append(next_node)
```

## 깊이 우선 탐색(Depth-First Search)
루트 노드에서 시작하여 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법

### 특징
* 트리 순회 알고리즘들은 DFS의 한 종류
* 어떤 노드를 방문했었는지 저장할 배열 필요
* 재귀 호출 가능
* Stack 자료구조로 구현

### 구현
```python
def dfs(graph, root):
    visited = list()
    stack = [root]
    while stack:
        node = stack.pop()
        if node no in visited:
            visited.append(node)
            for next_node in graph[node]:
                stack.append(next_node)
```

## 위상 정렬(Topological Sorting)
비순환 유향 그래프(Directed Acyclic Graph)의 꼭짓점들을 변의 방향을 거스르지 않도록 나열하는 것<br>
선후 관계가 정의된 그래프 구조 상에서 선후 관계에 따라 정렬하기 위해 사용

### 구현
구현은 Kahn의 알고리즘, DFS 두 가지로 가능하다.

* Kahn의 알고리즘
    1. 들어오는 엣지의 수가 0인 노드를 찾아 queue에 넣는다.
    2. queue에 있는 노드들의 outgoing edge를 제거한다.
    3. 1-2의 과정을 queue가 빌 때 까지 반복

* DFS
    * DFS 탐색 결과의 역순이 위상 정렬의 결과이다.
 