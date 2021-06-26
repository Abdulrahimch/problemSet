# time"2?:?0"

def latest_time(str):
    latest_time = ''

    if str[0] == '?':
        latest_time += '2'
    else:
        latest_time += str[0]

    if str[1] == '?':
        if str[0] == '2':
            latest_time += '3'
        else:
            latest_time += '9'

    if str[3] == '?':
        latest_time += ':5'
    else:
        latest_time += ':' + str[3]
    if str[4] == '?':
        latest_time += '9'
    else:
        latest_time += str[4]
    return latest_time
t1 = "2?:?0"
t2 = "1?:4?"
t3 = '0?:0?'
print(latest_time(t1))
print(latest_time(t2))
print(latest_time(t3))