a = ['classic', 'pop', 'classic', 'classic', 'pop']
b = [500, 600, 150, 800, 2500]
# should return [4, 1, 3, 0]

def solution(a,b):
    num = [i for i in range(len(a))]
    a = list(zip(a,b, num))
    s = {}
    counter = {}
    for i in a:
        if i[0] not in s:
            s[i[0]] = i[1]
            counter[i[0]] = 0
        else:
            s[i[0]] += i[1]
    a.sort(reverse = True, key = lambda x: (x[1]))
    s = sorted(s.items(), reverse = True, key = lambda x: x[1])
    answer = []
    for i in s:
        for j in a:
            if counter[i[0]] < 2 and i[0] == j[0]:
                answer.append(j[2])
                counter[i[0]] += 1

    return answer

print(solution(a,b))