a = ['classic', 'pop', 'classic', 'classic', 'pop', 'abc']
b = [500, 600, 150, 800, 2500, 10000]
# should return 4, 1, 3, 0

def solution(a,b):
    if len(a) < 1:
        return []
    elif len(a) == 1:
        return [0]
    total = {}
    counter = {}
    for i in range(len(a)):
        if a[i] not in total:
            total[a[i]] = b[i]
            counter[a[i]] = 0
        else:
            total[a[i]] += b[i]
        a[i] = [a[i],b[i],i]

    a.sort(key=lambda x:(x[0],x[1]), reverse = True)
    total = sorted(total, key = total.get, reverse = True)


    answer = []
    for i in total:
        for j in a:
            if counter[i] < 2 and i == j[0]:
                answer.append(j[2])
                counter[i] += 1
    
    return answer

print(solution(a,b))

