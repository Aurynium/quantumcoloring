# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C', 'E'],
#     'E': ['D']
# }

import queue

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}


q = []
str = ''
counter = 0
traversed = []

q.append('A')
q.append('-1')
while q:
    m = q.pop(0)

    if(m in traversed):
        continue
    if(m == '-1'):
        if(len(q) == 0):
            break
        counter += 1
        q.append('-1')
        continue

    if(counter%2 == 1):
        str += '~'
    
    str += m
    traversed.append(m)

    hasGoodNeighbors = False

    for neighbour in graph[m]:
        if neighbour not in traversed and neighbour not in q:
            hasGoodNeighbors = True
       
    for neighbour in graph[m]:
        if neighbour not in traversed and neighbour not in q:
            q.append(neighbour)

print(str)