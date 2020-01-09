a = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
# should return ['ICN', 'JFK', 'HND', 'IAD']
b = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
# should return [ICN, ATL, ICN, SFO, ATL, SFO]
c =  [['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], ['BOO', 'DOO'], ['DOO', 'BOO'],
['BOO', 'ICN'], ['COO', 'BOO']]

def solution(a):
    possible = {}
    a.sort(key = lambda x:x[1], reverse = True)
    for i in a:
        if i[0] not in possible:
            possible.setdefault(i[0],[])
            possible[i[0]].append(i[1])
        else:
            possible[i[0]].append(i[1])
    visited = ['ICN']
    path = []

    while len(visited) > 0:
        top = visited[-1]
        if top not in possible or len(possible[top]) == 0:
            path.append(visited.pop())
        else:
            visited.append(possible[top][-1])
            possible[top].pop()

    return path[::-1]

print(solution(b))