a = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
# should return 3 + 2 + 0 + 0 + 0 = 5
b = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
#should return 3 + 0 + 0 + 0 + 0 = 3
c = [['crow_mask', 'face'], ['blue_sunglasses', 'eyewear'], ['yellow_hat', 'headgear']]
#should return 3 + 1 + 1 + 1 + 1 = 7
def solution(a):
    a.sort(key = lambda x: x[1])
    category = {}
    result = 1
    for i in range(len(a)):
        if a[i][1] not in category:
            category[a[i][1]] = 1
        else:
            category[a[i][1]] += 1
    
    for i in category:
        result *= category[i] + 1


    return result - 1

print(solution(a))
print(solution(b))
print(solution(c))

