N, K = map(int, input().split())
A = list(map(int, input().split()))


def f(x):
    return (x + A[x % N]) % N


def calc_sum(L):
    ret = 0
    for t in L:
        ret += A[t]
    return ret


def naive():
    ans = 0
    rem = K
    while rem > 0:
        ans += A[ans % N]
        rem -= 1
    return ans


def cycle_detection(f, x0):
    """
    数列 A_{i+1} = f(A_i) のループの始点と周期を求める
    f: 関数 f(x)
    x0: A_0
    mu: ループの始点 A_{mu}
    lam: ループの周期 A_{mu} = A_{mu + k * lam}
    """
    power = lam = 1
    first = x0
    second = f(x0)

    while first != second:
        if power == lam:
            first = second
            power *= 2
            lam = 0
        second = f(second)
        lam += 1
    first = second = x0
    for i in range(lam):
        second = f(second)
    mu = 0
    while first != second:
        first = f(first)
        second = f(second)
        mu += 1
    return mu, lam


def cycle_detection_lists(f, x0):
    """サイクルに入る前・サイクルの中の数列そのものを返す"""
    mu, lam = cycle_detection(f, x0)
    before_cycle = [0] * mu
    if mu > 0:
        before_cycle[0] = x0
        for i in range(mu - 1):
            before_cycle[i + 1] = f(before_cycle[i])
    cycle = [0] * lam
    curr = x0 if mu == 0 else f(before_cycle[-1])
    cycle[0] = curr
    for i in range(lam - 1):
        cycle[i+1] = f(cycle[i])
    
    return before_cycle, cycle


def solve():
    # サイクルに入る前に終わるパターンの場合分けが面倒なので、Kが小さい場合は愚直解を返す
    if K <= N + 10:
        return naive()
    
    ans = 0
    rem = K
    bfc, cyc = cycle_detection_lists(f, 0)

    # サイクルに入る前の計算
    rem -= len(bfc)
    ans += calc_sum(bfc)

    # サイクルに入った後の計算
    q, r = divmod(rem, len(cyc))
    sum_cyc = calc_sum(cyc)
    ans += sum_cyc * q
    ans += calc_sum(cyc[:r])
    return ans

print(solve())