def per_cent(arr):
    for i in range(len(arr)):
        string = arr[i][2].split(".")[1]
        if string[0] == '0':
            string = string[1:]
        arr[i][2] = string + '%'
    return arr


def format_tel(arr):
    for i in range(len(arr)):
        arr[i][1] = arr[i][1].replace(' ', '')
    return arr


def divide_column(arr):
    tel = []
    names = []

    for i in range(len(arr[0])):
        tel_and_name = arr[0][i].split('#')
        tel.append((tel_and_name[0]))
        names.append(format_name((tel_and_name[1])))

    arr.pop(0)
    arr.insert(0, tel)
    arr.insert(0, names)

    return arr


def format_name(name):
    result = ''
    i = 0
    while i < len(name):
        if name[i] == ' ':
            i += 3
            result += name[i].upper()
        else:
            result += name[i]
        i += 1

    return result


def last_name(arr):
    for i in range(len(arr)):
        arr[i][0] = arr[i][0].split('.')[1].replace(' ', '')
    return arr


def first_symbol_for_line(line):
    is_word = line == 'да' or line == 'нет'
    if not is_word:
        return line

    if line == 'да':
        line = 'Да'
    elif line == 'нет':
        line = 'Нет'

    return line


def get_column(arr, index):
    column = []
    for i in range(len(arr)):
        column.append(arr[i][index])
    return column


def transpose(arr):
    new_arr = []

    for i in range(len(arr[0])):
        new_arr.append(get_column(arr, i))
    return new_arr


def delete_equal_lines(arr, index):
    result = False
    i = index + 1
    while i < len(arr):
        if arr[index] == arr[i]:
            arr.pop(i)
            result = True
            i -= 1
        i += 1
    return [arr, result]


def delete_none_lines(arr):
    i = 0
    while i < len(arr):
        if arr[i][0] is None:
            arr.pop(i)
            i -= 1
        i += 1
    return arr


def format_mail(arr):
    for i in range(len(arr)):
        arr[i][3] = arr[i][3].replace('[at]', '@')
    return arr


def solve(arr):
    tab = arr
    i = 0
    while i < len(tab):
        temp = delete_equal_lines(tab, i)
        tab = temp[0]
        if temp[1]:
            i -= 1
        i += 1

    transpose(tab)
    tab = delete_none_lines(tab)
    tab = transpose(tab)
    tab = divide_column(tab)
    tab = transpose(tab)
    tab = per_cent(tab)
    tab = format_tel(tab)
    tab = format_mail(tab)

    return tab


def main(h):
    return solve(h)