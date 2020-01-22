a = "photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmy-Friends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.ipg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40: 22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:5:32\ng.jpg, Warsaw, 2016-02-29 22:13:11"

# should return Warsaw02.jpg London1.png Warsaw01.png Paris2.jpg Paris1.jpg London2.jpg Paris3.jpg Warsaw03.jpg Warsaw09.jpg Warsaw07.jpg Warsaw06.jpg Warsaw08.jpg Warsaw04.jpg Warsaw05.jpg Warsaw10.jpg
from datetime import datetime as dt

def solution(a):
    a = a.split('\n')
    s = []
    c = 0
    for i in a:
        e = i.split(',')
        title = e[0]
        name = e[1].strip()
        date_time = e[2].replace(' ', '')
        date= ''.join(date_time[:10])
        time = ''.join(date_time[10:])
        date_time = date + ' ' + time
        d = dt.strptime(date_time,'%Y-%m-%d %H:%M:%S')
        ext = title.split('.')[1]
        s.append((name, ext, d, c))
        c += 1
    s.sort(key=lambda x: (x[0],x[2]))   
    
    f = []
    check = []
    counter = 1
    for i in s:
        if i[0] not in check:
            counter = 1
            check.append(i[0])
            f.append((i[0]+str(counter).zfill(2)+'.'+i[1], i[3]))
        else:
            counter += 1
            f.append((i[0]+str(counter).zfill(2)+'.'+i[1], i[3]))

    f.sort(key=lambda x: x[1])
    answer = ''
    for i in f:
        answer += (i[0] + ' ')

    return answer

print(solution(a))