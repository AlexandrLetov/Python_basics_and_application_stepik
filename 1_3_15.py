n, k = map(int, input().split())


def comb(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return comb(n-1, k) + comb(n-1, k-1)


print(comb(n, k))
