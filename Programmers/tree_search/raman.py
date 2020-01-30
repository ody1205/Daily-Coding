
import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    supplies = [i*(-1) for i in supplies]
    li = list(zip(supplies, dates))
    heapq.heapify(li)
    while stock < k:
        supply = heapq.heappop(li)
        stock -= supply[0]
        answer += 1

    return answer

st = 4
d = [4,10,15]
su = [20,5,10]
k = 30
print(solution(st,d,su,k))
'''
stock of 4 will be gone at day 4.
should get supply at day 4, which will fill up 20
you can skip day 10 supply since you can last until day 15 to get 10
which will give us 11 + 10 = 21 at day 15 which is more than enough
to last until target date 30.
should return 2 as we get supplied twice in total.
'''

st = 4
d = [1, 2, 3, 4]
su = [10, 40, 30, 20]
k = 100
print(solution(st,d,su,k))

