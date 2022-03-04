def a():
    b = 1
    if b == 1:
        return 1

    c = 1 + 2
    return c


if a() == 1:
    print('最初のreturn')
else:
    print('2回目のreturn')
