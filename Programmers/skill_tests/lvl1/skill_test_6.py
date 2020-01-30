def solution(N, stages):
    answer = []
    p_num = len(stages)
    stages.sort()
    a = {}
    for i in stages:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    for j in a:
        answer.append([a[j]/p_num, j])
        p_num -= a[j]
    stage = {i+1:0 for i in range(N)}
    for i in answer:
        if i[1] in stage:
            stage[i[1]] = i[0]
    x = sorted(stage, key=stage.get,reverse=True)

    return x

n = 5
s = [2,1,2,6,2,4,3,3]
print(solution(n, s))
# should return 3,4,2,1,5
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수