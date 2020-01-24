def solution(genres, plays):
    answer = []

    dic = {}
    for idx, category in enumerate(genres):
        if category not in dic:
            dic[category] = [0, ]

        play_time = plays[idx]
        dic[category].append((idx, play_time))
        dic[category][0] += play_time

    categories = list(dic.keys())
    categories.sort(key = lambda x : dic[x][0], reverse=True)

    for category in categories:
        play_list = dic[category][1:]
        play_list.sort(key = lambda x:x[1], reverse=True)
        print(play_list)

        for i in range(len(play_list)):
            if i == 2:
                break

            answer.append(play_list[i][0])

    return answer

a = ['classic', 'pop', 'classic', 'classic', 'pop']
b = [500, 600, 150, 800, 2500]
# should return 4, 1, 3, 0
print(solution(a,b))