'''

'''
from collections import defaultdict
def solution(a,w):
    s = defaultdict(list)
    link = defaultdict(list)
    w = w.lower()
    k = 0
    for i in a:
        website = ''
        for j in (i.split('\n')):
            for z in j.split(' '):
                if 'content' in z.split('='):
                    website = z.split('=')[1].strip('>').strip('/').strip('"')
                    s[website] = [0, k]
                    k += 1
                if 'href' in z.split('='):
                    link[website].append(z.split('=')[1].strip('>').strip('"'))
                if z.lower() == w:
                    s[website][0] += 1
    print(link)
    add_to = []
    for i in link:
        num_link = len(link[i])
        for j in link[i]:
            add_to.append((j,s[i][0]/num_link))
    print(add_to)
    for i,j in add_to:
        s[i][0] += j

    return s[max(s, key=s.get)][1]
a = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(a,'Muzi'))