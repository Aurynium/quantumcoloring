
# Adjacency list representation of the graph of countries
graph = {
    'A': ['B','E','F','I'],
    'B': ['A','C','D'],
    'C': ['B','F'],
    'D': ['B','E','L'],
    'E': ['A','D','H','J'],
    'F': ['A','C','G'],
    'G': ['F','I'],
    'H': ['E','I','K'],
    'I': ['A','G','H'],
    'J': ['E','K','L'],
    'K': ['H','J'],
    'L': ['D','J']
}

# Initialize a queue variable q, an empty string variable str,
# an integer variable counter, and an empty array traversed
q = []
str = ''
counter = 0
traversed = []

# Append the first element of the graph
q.append(list(graph.keys())[0])
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
    str += ' & '
    traversed.append(m)

    hasGoodNeighbors = False

    for neighbour in graph[m]:
        if neighbour not in traversed and neighbour not in q:
            hasGoodNeighbors = True
       
    for neighbour in graph[m]:
        if neighbour not in traversed and neighbour not in q:
            q.append(neighbour)

str = str[0:len(str)-3]

print(str)