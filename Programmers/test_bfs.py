def bfs(graph, s):
    possible = {}
    a.sort(key = lambda x:x[1])
    for i in a:
        if i[0] not in possible:
            possible.setdefault(i[0],[])
            possible[i[0]].append(i[1])
        else:
            possible[i[0]].append(i[1])
    visited = [False] * len(graph)
    q = []
    q.append(s)
    visited[possible[s].index(s)] = True
    while q:
        s = q.pop(0)
        print(s)
        for i in graph[s]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

a = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]

print(bfs(a, 'HND'))