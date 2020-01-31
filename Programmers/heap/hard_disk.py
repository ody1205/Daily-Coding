a =[[0, 3], [1, 9], [2, 6]]

import heapq
def solution(a):
    length = []
    for i in a:
        length.append((i[1]+i[0], i))
    length.sort(key=lambda x: x[0])
    print(length)
    total = [length[0][1][1]]
    for i in range(len(length)-1):
        total.append(length[i][1][1] - length[i+1][1][0] + length[i+1][1][1] + sum(total[:i]))
    avg = sum(total) // len(total)
    return avg

print(solution(a))