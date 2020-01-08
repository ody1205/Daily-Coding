a = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
# should return ['ICN', 'JFK', 'HND', 'IAD']
b = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
# should return [ICN, ATL, ICN, SFO, ATL, SFO]
c =  [['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], ['BOO', 'DOO'], ['DOO', 'BOO'],
['BOO', 'ICN'], ['COO', 'BOO']]

def solution(a):
    possible = {}
    answer = 0
    visited = []
    a.sort(key = lambda x:x[1])
    for i in a:
        if i[0] not in possible:
            possible.setdefault(i[0],[])
            possible[i[0]].append(i[1])
        else:
            possible[i[0]].append(i[1])
    # visit = [False] * len(a)
    print(a)
    prev = ''
    # print(visit)
    while len(possible) > 0:
        for air_port in possible:
            if air_port == 'ICN' and air_port not in visited:
                visited.append(air_port)
                prev = possible[air_port][0]
                possible[air_port].pop(0)
                visited.append(prev)

                if len(possible[air_port]) < 1:
                    possible.pop(air_port)
                    break
            elif air_port == 'ICN' and air_port in visited:
                prev = possible[air_port][0]
                possible[air_port].pop(0)
                visited.append(prev)

                if len(possible[air_port]) < 1:
                    possible.pop(air_port)
                    break
            elif air_port == prev:
                prev = possible[air_port][0]
                possible[air_port].pop(0)
                visited.append(prev)

                if len(possible[air_port]) < 1:
                    possible.pop(air_port)
                    break

    return visited

print(solution(a))