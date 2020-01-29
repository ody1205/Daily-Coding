
def solution(b_l, w, t_w):
    bridge = [0] * b_l
    answer = 0
    while bridge:
        answer += 1
        bridge.pop(0)
        if t_w:
            if sum(bridge) + t_w[0] <= w:
                bridge.append(t_w.pop(0))
            else:
                bridge.append(0)

    return answer


b = 100
w = 100
t = [10]
print(solution(b,w,t))