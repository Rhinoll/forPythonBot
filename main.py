import math


def main1(x):
    if x < 20:
        return (29 * x) ** 7 - math.sin(x) ** 2
    elif 20 <= x < 55:
        return (x ** 2) / 95 + 12 * (1 + x + (x ** 3) / 28) ** 4 + (x ** 6) / 83
    elif 55 <= x < 147:
        return 54 * math.cos(x) ** 4 + x / 57
    elif 147 <= x < 173:
        return 53 * x + 92 * ((x ** 2) / 39) ** 3
    else:
        return (19 * x) ** 7 - 98 * (x ** 4)


def main2(n, z, b, p):
    sum1, sum2, sum3 = 0, 0, 0
    for i in range(1, n + 1):
        sum1 += ((9 * (z ** 2) + z) ** 3 - (i + 29 + z ** 3) ** 7)
    for k in range(1, n + 1):
        for c in range(1, b + 1):
            sum2 += ((k ** 5) / 79 + 15 * (89 + c ** 2 + p) ** 4)
        sum3 += sum2
        sum2 = 0

    return sum1 + sum3


print(main2(3, -0.57, 8, 0.38))
# print(main2(4, -0.59, 7, -0.99))

def main3(n):
    if n == 0:
        return 0.52
    elif n == 1:
        return 0.06
    elif n >= 2:
        return (main3(n - 2) ** 2) / 37 + 1 + main3(n - 1)


# print(main3(5))

def main(lst):
    def vector(a):
        return (a ** 2 + 1 + 90 * a ** 3) ** 7

    res = 0
    for i in lst:
        res += vector(i)

    return 86 * res


main([0.51, -0.68, -0.17, 0.14])


def f(*lst):
    def fun(a, b):
        return (22 * a + 1 + 13 * b ** 2) ** 7

    z, x = lst
    res = 0
    for i in range(len(x)):
        res += fun(z[i // 3], x[i])

    print(f'{73 * res:.2e}')


f([-0.15, 0.43], [-0.04, -0.81])
f([0.79, -0.12], [-0.5, -0.53])
