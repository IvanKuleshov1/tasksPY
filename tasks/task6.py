def zero(items, left, middle, right):
    if items[0] == 1963:
        return left
    if items[0] == 1985:
        return middle
    if items[0] == 1987:
        return right


def two(items, left, middle, right):
    if items[2] == 'E':
        return left
    if items[2] == "SCSS":
        return middle
    if items[2] == 'LIMBO':
        return right


def three(items, left, middle, right):
    if items[3] == 1974:
        return left
    if items[3] == 2007:
        return middle
    if items[3] == 1997:
        return right


def main(items):
    return three(
        items,
        two(
            items,
            zero(items, 0, 1, 2),
            zero(items, 3, 4, 5),
            zero(items, 6, 7, 8)
        ),
        zero(items, two(items, 9, 10, 11), 12, 13), 14)


print(main([1987, 'BLADE', 'SCSS', 1997]))
