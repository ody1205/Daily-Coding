import heapq

def solution(scoville, K):
    answer = 0
    # k is target scoville
    # the goal is to make every scoviile list above K by mixing them
    # new_scoville = old_scoville(lower one) + (old_scoville(higher one) * 2)
    heapq.heapify(scoville)

    while len(scoville) > 1 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b*2))
        answer += 1
    if scoville[0] < K:
        return -1
    else:
        return answer
        


s = [1,2,3,9,10,12]
k = 7
print(solution(s,k))
# should return 2