a = ['classic', 'pop', 'classic', 'classic', 'pop']
b = [500, 600, 150, 800, 2500]
# should return 4, 1, 3, 0

def solution(a,b):
    if len(a) < 1:
        return []
    elif len(a) == 1:
        return [0]
        
    total = {}
    for i in range(len(a)):
        if a[i] not in total:
            total[a[i]] = b[i]
        else:
            total[a[i]] += b[i]
        a[i] = [a[i],b[i],i]

    a.sort(key=lambda x:(x[0],x[1]), reverse = True)
    total = sorted(total, key = total.get, reverse = True)

    two = 0
    answer = []
    for i in total:
        for j in a:
            if two < 2:
                if i == j[0]:
                    answer.append(j[2])
                    two += 1
            else:
                two = 0
                break
    
    return answer

print(solution(a,b))

