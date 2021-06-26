import math



def shortestToChar(s, c):
    answer = []
    c_idx = []
    s_list = s.split()
    min_distance = math.inf
    s_list = [i for i in s]

    for i in range(len(s_list)):
        if s_list[i] == c:
            c_idx.append(i)
            s_list[i] = '-'
    s = ''.join(s_list)

    distance = []
    for j in range(len(s)):
        if s[j] == '-':
            answer.append(0)
            continue
        for k in c_idx:
            distance = abs(j - k)
            if distance < min_distance:
                min_distance = distance
        answer.append(min_distance)
        min_distance = math.inf

    return answer