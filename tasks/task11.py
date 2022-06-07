from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d',
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1_size, offs = parse(buf, offs, 'uint32')
    a1_offs, offs = parse(buf, offs, 'uint32')
    a1 = []
    for _ in range(a1_size):
        val, a1_offs = parse(buf, a1_offs, 'char')
        a1.append(val.decode())
    a2, offs = parse(buf, offs, 'int32')
    a3, offs = parse(buf, offs, 'uint32')
    a4_offs, offs = parse(buf, offs, 'uint32')
    a4 = []
    for _ in range(a4_offs):
        val, a4_offs = parse_b(buf, a4_offs)
        a4.append(val)
    a5, offs = parse(buf, offs, 'int8')
    a6, offs = parse(buf, offs, 'uint32')
    a7, offs = parse_e(buf, offs)
    a8, offs = parse(buf, offs, 'double')

    return dict(A1=''.join(a1), A2=a2, A3=a3, A4=a4,
                A5=a5, A6=a6, A7=a7, A8=a8), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'uint8')
    b2, offs = parse(buf, offs, 'int8')
    b3_size, offs = parse(buf, offs, 'uint32')
    b3_offs, offs = parse(buf, offs, 'uint32')
    b3 = []
    for _ in range(b3_size):
        val, b3_offs = parse_c(buf, b3_offs)
        b3.append(val)
    b4, offs = parse_d(buf, offs)
    b5, offs = parse(buf, offs, 'uint8')
    b6, offs = parse(buf, offs, 'int8')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6), offs


def parse_c(buf, offs):
    c1 = []
    for _ in range(4):
        val, offs = parse(buf, offs, 'uint8')
        c1.append(val)
    c2_size, offs = parse(buf, offs, 'uint16')
    c2_offs, offs = parse(buf, offs, 'uint16')
    c2 = []
    for _ in range(c2_size):
        val, b2_offs = parse(buf, c2_offs, 'int64')
        c2.append(val)
    c3, offs = parse(buf, offs, 'int16')

    return dict(C1=c1, C2=c2, C3=c3), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'uint16')
    d2, offs = parse(buf, offs, 'uint32')
    d3, offs = parse(buf, offs, 'uint32')
    return dict(D1=d1, D2=d2, D3=d3), offs


def parse_e(buf, offs):
    e1, offs = parse(buf, offs, 'int16')
    e2, offs = parse(buf, offs, 'int32')
    return dict(E1=e1, E2=e2), offs


def main(buf):
    return parse_a(buf, 4)[0]


print(main((b'\xf8UQJ>S4\xbf\nK*\x7fB\x8b/\xc8\x04\x00E\x00\x00\x00\xc1c\xb54\x03K'
            b'\x84K\xec\x7f\x15\x8d\xd2l\x9e\x03\x00\x00\x00\x8d\x00x\xc0\x9a\xfe@'
            b'{\x1c\x83\x84\x85\x14<\x1e\xe4.\xd3\xeb\x19\x03\x00\x00\x00\x90\x00\xa5'
            b'\xf8\xbb$\x9f\r\xa4\xc6\xa8H\xe2C\x16w\x00\xd6\x11\xc2\x0b\xf0H\xe2\xaa\x1an'
            b'\xca&\x99j\x98f\xe2H\x93L.iA\xa8\x18\x13\xe4sM\x9f\xc7\xa9\xd2J\xd1a\xd7V'
            b'\\\xf5\x08\xffs\xd4\xbb\xb1\x84\xfd\xcdG\xc3\xa8\xc8):\xcf\x03\x0f\xd5xno'
            b'x\xd4\xb9')))
