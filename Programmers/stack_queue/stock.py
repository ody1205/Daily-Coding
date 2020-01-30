

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        print('i',i)
        for j in range(i, len(prices)-1):
            print(j)
            if prices[i] > prices[j]:
                break
            else:
                answer[i] +=1
    return answer

p = [1, 2, 3, 2, 3]
print(solution(p))