a = ['classic', 'pop', 'classic', 'classic', 'pop']
b = [500, 600, 150, 800, 2500]
# should return [4, 1, 3, 0]

def solution(genre,play_time):
    num = [i for i in range(len(genre))]
    genre = list(zip(genre, play_time, num))
    # combine genre, play_time and original position in a list
    total = {}
    # dictionary to hold sums of play_time for each genre
    counter = {}
    # counter to keep track of each genre being played twice
    for i in genre:
        if i[0] not in total:
            total[i[0]] = i[1]
            counter[i[0]] = 0
        else:
            total[i[0]] += i[1]
    # sum up the play_time for each genre

    genre.sort(reverse = True, key = lambda x: (x[1]))
    total = sorted(total.items(), reverse = True, key = lambda x: x[1])
    
    answer = []
    
    for i in total:
        for j in genre:
            if counter[i[0]] < 2 and i[0] == j[0]:
                answer.append(j[2])
                counter[i[0]] += 1

    return answer

print(solution(a,b))