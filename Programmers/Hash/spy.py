a = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
# should return 5
b = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]

def solution(clothes):
    total_per_kind = {}
    # keep track of counts per each kind of clothes
    for kind in clothes:
        if kind[1] not in total_per_kind:
            total_per_kind[kind[1]] = 1
        else:
            total_per_kind[kind[1]] += 1
    # since you can either wear a kind of cloth or not wear one
    # add one to each kind of clothes
    for i in total_per_kind:
        total_per_kind[i] += 1
    
    # calculate total possible scenario by multiplying them together 
    answer = 1
    for i in total_per_kind:
        answer *= total_per_kind[i]

    return answer - 1
    # take one scenario off which is not wearing any kind of clothes

print(solution(a))
print(solution(b))