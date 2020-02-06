def solution(numbers, target):
    answer_list = [0]
    for i in numbers:
        temp = []
        for j in answer_list:
            temp.append(j - i)
            temp.append(j + i)
        answer_list = temp
    answer = answer_list.count(target)
    return answer


num = [1, 1, 1, 1, 1]
target = 3
print(solution(num,target))
#should return 5