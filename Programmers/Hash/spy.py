a = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
# should return 5
b = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
def solution(a):
    s = {}
    for i in a:
        if i[1] not in s:
            s[i[1]] = 1
        else:
            s[i[1]] += 1
    answer = 1
    for i in s:
        s[i] += 1
    
    for i in s:
        answer *= s[i]

    return answer - 1

print(solution(a))
print(solution(b))