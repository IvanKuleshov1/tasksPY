import math


def main(listx, listy):
    res = 0
    for i in range(1, 3):
        res += 38 * (listy[2 - math.ceil(i / 4)] ** 3 / 91
                     - 1 - listx[2 - math.ceil(i / 2)]**2) ** 7
    return res


print(main([-0.56, -0.71], [-0.31, 0.0]))
