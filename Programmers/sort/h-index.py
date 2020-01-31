# def solution(citations):
#     citations.sort(reverse=True)
#     return max(map(min, enumerate(citations, start=1)))

def solution(citations):
  sorted_citations = sorted(citations, reverse=True)
  for i in range(len(sorted_citations)):
    if sorted_citations[i] <= i: 
      return i
  return len(sorted_citations)


c = [3,0,6,1,5]
print(solution(c))
# should return 3

# print(solution([10, 50 ,100]))
# # should return 3