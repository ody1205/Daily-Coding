def solution(priorities, location):
    priorities = [(priority, idx) for idx, priority in enumerate(priorities)]
    queue = []
    
    while priorities:
        temp = priorities.pop(0)
        priority = temp[0]
        p_list = [i for i, idx in priorities]
        if p_list:
            max_p = max(p_list)

        if max_p <= priority:
            queue.append(temp)
        else:
            priorities.append(temp)

    
    for idx, item in enumerate(queue):
        if location == item[1]:
            return idx + 1


# p = [2,1,3,2]
# l = 2
# print(solution(p,l))
# # should return 1

p1 = [1,1,9,1,1,1]
l1 = 0
print(solution(p1,l1))
# should return 5