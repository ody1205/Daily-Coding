import math
def solution(progresses, speeds):
    answer = []
    length = [0] * len(speeds)
    for i in range(len(speeds)):
        left = 100 - progresses[i]
        length[i] += math.ceil(abs(left/speeds[i]))
    
    for i in range(1,len(length)):
        if length[i-1] > length[i]:
            length[i] = length[i-1]
    
    count = 1
    for i in range(1,len(length)):
        if length[i-1] >= length[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
    answer.append(count)

    return answer


p = [93,30,55]
s = [1,30,5]
# should return [2,1]
print(solution(p,s))