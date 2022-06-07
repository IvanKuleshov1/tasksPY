from struct import unpack_from, calcsize
from typing import Any, Callable


class BinaryReader:
    def __init__(self, source, offset=0):
        self.offset = offset
        self.source = source

    def read_uint64(self):
        return self.read('Q')

    def read_int64(self):
        return self.read('q')

    def read_uint32(self):
        return self.read('I')

    def read_int32(self):
        return self.read('i')

    def read_uint16(self):
        return self.read('H')

    def read_int16(self):
        return self.read('h')

    def read_uint8(self):
        return self.read('B')

    def read_int8(self):
        return self.read('b')

    def read_float(self):
        return self.read('f')

    def read_char(self):
        return self.read('c')

    def read_double(self):
        return self.read('d')

    def read(self, pattern: str):
        size = calcsize(pattern)
        data = unpack_from(pattern, self.source, self.offset)
        self.offset += size
        return data[0]


def read_array(
        source: str,
        size: int,
        address: int,
        read: Callable[[BinaryReader], Any],
        structure_size: int = 1,
):
    reader = BinaryReader(source, address)
    values = []
    while address + (size * structure_size) > reader.offset:
        values.append(read(reader))
    return values


def read_e(reader: BinaryReader):
    e1 = reader.read_int16()
    e2 = reader.read_int32()
    return dict(E1=e1, E2=e2)


def read_d(reader: BinaryReader):
    d1 = reader.read_uint16()
    d2 = reader.read_int32()
    d3 = reader.read_uint32()
    return dict(D1=d1, D2=d2, D3=d3)


def read_c(reader: BinaryReader):
    c1 = [reader.read_uint16(), reader.read_uint16(),
          reader.read_uint16(), reader.read_uint16()]
    c2 = read_array(
        source=reader.source,
        size=reader.read_uint32(),
        address=reader.read_uint32(),
        read=lambda reader: read_c(reader)
    )
    c3 = reader.read_int16()
    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader: BinaryReader):
    b1 = reader.read_uint8()
    b2 = reader.read_int8()
    b3 = read_array(
        source=reader.source,
        size=reader.read_uint32(),
        address=reader.read_uint32(),
        read=lambda reader: read_c(reader)
    )
    b4 = read_d(reader)
    b5 = reader.read_uint8()
    b6 = reader.read_int8()
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6)


def read_a(reader: BinaryReader):
    a1 = ''.join(
        read_array(
            source=reader.source,
            size=reader.read_uint32(),
            address=reader.read_uint32(),
            read=lambda reader: reader.read_char().decode('ascii')
        )
    )
    a2 = reader.read_int32()
    a3 = reader.read_uint32()
    a4 = ''.join(
        read_array(
            source=reader.source,
            address=reader.read_uint32(),
            read=lambda reader: read_b(reader)
        )
    )
    a5 = reader.read_int8()
    a6 = reader.read_uint32()
    a7 = read_e(reader)
    a8 = reader.read_double()
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8)


def main(source):
    reader = BinaryReader(source)
    reader.read('cccc')
    return read_a(reader)

print(main((b'\xf8UQJ>S4\xbf\nK*\x7fB\x8b/\xc8\x04\x00E\x00\x00\x00\xc1c\xb54\x03K'
            b'\x84K\xec\x7f\x15\x8d\xd2l\x9e\x03\x00\x00\x00\x8d\x00x\xc0\x9a\xfe@'
            b'{\x1c\x83\x84\x85\x14<\x1e\xe4.\xd3\xeb\x19\x03\x00\x00\x00\x90\x00\xa5'
            b'\xf8\xbb$\x9f\r\xa4\xc6\xa8H\xe2C\x16w\x00\xd6\x11\xc2\x0b\xf0H\xe2\xaa\x1an'
            b'\xca&\x99j\x98f\xe2H\x93L.iA\xa8\x18\x13\xe4sM\x9f\xc7\xa9\xd2J\xd1a\xd7V'
            b'\\\xf5\x08\xffs\xd4\xbb\xb1\x84\xfd\xcdG\xc3\xa8\xc8):\xcf\x03\x0f\xd5xno'
            b'x\xd4\xb9')))