b = 10	
r = 2	# [4, 3]
b1 = 8
r1 = 1	# [3, 3]
b2 = 24
r2 = 24# [8, 6]

b3 = 81344
r3 = 1000000

def solution(brown, red):
    # x * y = brown + red
    # (x-2) * (y-2) = red
    # 2x^2 - (brown+4)x + 2red + 2brown = 0
    # x = (brown+4) + sqrt((brown+4)^2 - 8 * (2brown + 2red)) / 4
    # y = (brown + red) / x
    x = ((brown + 4) + ((brown+4)**2 - 16 * (brown + red)) ** 0.5) / 4
    y = (brown + red) // x
    return [int(max(x,y)), int(min(x,y))]

print(solution(b,r))
# 4,3
print(solution(b1,r1))
# 3,3
print(solution(b2,r2))
# 8,6
# print(solution(b3,r3))