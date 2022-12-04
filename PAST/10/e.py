y, m, d= map(int, input().split('/'))

def int_to_str(_integer):
    temp = []
    _string = str(_integer)
    for i in range(len(_string)):
        temp.append(_string[i])
    return temp

def show_ans(temp):
    year = "".join(temp[:4])
    month = "".join(temp[4:6])
    date = "".join(temp[6:])
    print(year + "/" + month + "/" + date)

def solve(y, m, d):
    temp = []
    y_list = int_to_str(y)
    temp += y_list
    if m < 9:
        temp.append(0)
        temp.append(m)
    else:
        m_list = int_to_str(m)
        temp += m_list
    if d < 9:
        temp.append(0)
        temp.append(d)
    else:
        d_list = int_to_str(d)
        temp += d_list
    temp = [str(x) for x in temp]
    cnt = len(set(temp))
    if cnt < 3:
        show_ans(temp)
        exit()


for i in range(2000):
    for j in range(14):
        for k in range(33):
            if d > 31:
                d = 1
                break
            solve(y, m, d)
            d += 1
        if m > 12:
            d = 1
            m = 1
            break
        m += 1
    y += 1
    m = 1
    d = 1


import datetime
D = datetime.date.fromisoformat(input().replace('/', '-'))
while len({c for c in D.isoformat()}) > 3:
  D += datetime.timedelta(days=1)
print(D.isoformat().replace('-', '/'))