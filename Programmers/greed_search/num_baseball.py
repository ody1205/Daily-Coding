b = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

from itertools import permutations

def get_score(request, number):
    strikes, balls = (0,0)
    for i in range(3):
        if request[i] == number[i]:
            strikes += 1
        elif request[i] in number:
            balls += 1
    return (strikes, balls)

def solution(baseball):
    answer = 0
    possible = [str(i) for i in range(1,10)]
    perm_p = list(permutations(possible,3))
    perm = [''.join(i) for i in perm_p]

    for request, strike, ball in baseball:
        for number in perm:
            perm = [number for number in perm if get_score(str(request),number) == (strike, ball)]
    return len(perm)

print(solution(b))