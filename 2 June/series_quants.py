n = 10
a = 2
d = 3
k = 5
A = 1
B = -5
C = 6


def sum(n):
    return int((n * (n+1)) / 2)


def sum_sq(n):
    res = 0
    for i in range(n+1):
        res += i**2
    return res


def arth_sum(k, a, d):
    return int((k / 2) * (2 * a + (k - 1) * d))


def disc(A, B, C):
    return int(B**2 - 4*A*C)


def roots(A, B, C):
    x = (-B + (disc(A, B, C) ** (1/2))) / 2 * A
    y = (-B - (disc(A, B, C) ** (1/2))) / 2 * A
    return str(x), str(y)


def vertex(A, B):
    return -B / (2 * A)


def optimal_val(A, B, C):
    res = C - ((B**2) / (4 * A))
    return str(res), "(Minimum)" if A > 0 else "(Maximum)"


print(sum(n))
print(sum_sq(n))
print(arth_sum(k, a, d))
print(disc(A, B, C))
res = roots(A, B, C)
res = " ".join(res)
print(res)
print(vertex(A, B))
res = optimal_val(A, B, C)
res = " ".join(res)
print(res)
