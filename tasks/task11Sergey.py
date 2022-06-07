import struct

BYTE_INDEX = 0


def my_repack(type, arr):
    global BYTE_INDEX
    BYTE_INDEX += len(arr)
    return struct.unpack(type, arr)[0]


class structE:
    def fill_struct(self, b):
        global BYTE_INDEX

        self.set_E1(my_repack('>h', b[BYTE_INDEX: BYTE_INDEX + 2]))
        self.set_E2(my_repack('>i', b[BYTE_INDEX: BYTE_INDEX + 4]))

        return self

    def set_E1(self, a):
        self.E1 = a

    def set_E2(self, a):
        self.E2 = a

    def get_cort(self):
        return {'E1': self.E1, 'E2': self.E2}


class structD:
    def fill_struct(self, b):
        global BYTE_INDEX

        self.set_D1(my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2]))
        self.set_D2(my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4]))
        self.set_D3(my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4]))

        return self

    def set_D1(self, a):
        self.D1 = a

    def set_D2(self, a):
        self.D2 = a

    def set_D3(self, a):
        self.D3 = a

    def get_cort(self):
        return {'D1': self.D1,
                'D2': self.D2,
                'D3': self.D3}


class structC:
    def fill_struct(self, b):
        global BYTE_INDEX

        arr_uint8 = []

        for i in range(4):
            arr_uint8.append(my_repack('>B', b[BYTE_INDEX: BYTE_INDEX + 1]))

        self.set_C1(arr_uint8)
        size = my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2])
        pointer = my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2])

        STOP_INDEX = BYTE_INDEX
        BYTE_INDEX = pointer

        arr1 = []

        for i in range(size):
            arr1.append(my_repack('>q', b[BYTE_INDEX: BYTE_INDEX + 8]))

        self.set_C2(arr1)

        BYTE_INDEX = STOP_INDEX
        self.set_C3(my_repack('>h', b[BYTE_INDEX: BYTE_INDEX + 2]))

        return self

    def set_C1(self, a):
        self.C1 = a

    def set_C2(self, a):
        self.C2 = a

    def set_C3(self, a):
        self.C3 = a

    def get_cort(self):
        arr = []

        for i in self.C1:
            arr.append(i.get_cort())
        return {'C1': arr,
                'C2': self.C2,
                'C3': self.C3}


class structB:
    def fill_struct(self, b):
        global BYTE_INDEX

        arr_C = []

        for i in range(2):
            arr_C.append(structC().fill_struct(b))

        self.set_B1(arr_C)

        self.set_B1(my_repack('>b', b[BYTE_INDEX: BYTE_INDEX + 1]))
        self.set_B2(my_repack('>B', b[BYTE_INDEX: BYTE_INDEX + 1]))

        size = my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4])

        pointer = my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4])

        STOP_INDEX = BYTE_INDEX
        BYTE_INDEX = pointer

        arr_c = []

        for i in range(size):
            arr_c.append(my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4]))

        self.set_B2(arr_c)

        BYTE_INDEX = STOP_INDEX
        self.set_B4(structD().fill_struct(b))
        self.set_B5(my_repack('>B', b[BYTE_INDEX: BYTE_INDEX + 1]))
        self.set_B6(my_repack('>b', b[BYTE_INDEX: BYTE_INDEX + 1]))

        return self

    def set_B1(self, a):
        self.B1 = a

    def set_B2(self, a):
        self.B2 = a

    def set_B3(self, a):
        self.B3 = a

    def set_B4(self, a):
        self.B4 = a

    def set_B5(self, a):
        self.B5 = a

    def set_B6(self, a):
        self.B6 = a

    def get_cort(self):
        arr = []

        for i in self.B1:
            arr.append(i.get_cort())

        return {'B1': self.B1,
                'B2': self.B2,
                'B3': self.B3,
                'B4': self.B4.get_cort(),
                'B5': self.B5,
                'B6': self.B6}


class structA:
    def fill_struct(self, b):
        global BYTE_INDEX

        size = my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4])

        pointer = my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4])

        STOP_INDEX = BYTE_INDEX
        BYTE_INDEX = pointer

        arr_char = []

        for i in range(size):
            arr_char.append(my_repack('>c', b[BYTE_INDEX: BYTE_INDEX + 1]))

        self.set_A1(arr_char)
        BYTE_INDEX = STOP_INDEX
        self.set_A2(my_repack('>i', b[BYTE_INDEX: BYTE_INDEX + 4]))
        self.set_A3(my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4]))
        BYTE_INDEX = STOP_INDEX

        pointer = my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4])

        STOP_INDEX = BYTE_INDEX
        BYTE_INDEX = pointer

        self.set_A4(structB().fill_struct(b))

        BYTE_INDEX = STOP_INDEX
        self.set_A5(my_repack('>b', b[BYTE_INDEX: BYTE_INDEX + 1]))
        self.set_A6(my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4]))
        self.set_A7(structE().fill_struct(b))
        self.set_A8(my_repack('>d', b[BYTE_INDEX: BYTE_INDEX + 8]))
        return self

    def set_A1(self, a):
        self.A1 = a

    def set_A2(self, a):
        self.A2 = a

    def set_A3(self, a):
        self.A3 = a

    def set_A4(self, a):
        self.A4 = a

    def set_A5(self, a):
        self.A5 = a

    def set_A6(self, a):
        self.A6 = a

    def set_A7(self, a):
        self.A7 = a

    def set_A8(self, a):
        self.A8 = a

    def get_cort(self):
        return {'A1': self.A1,
                'A2': self.A2,
                'A3': self.A3,
                'A4': self.A4.get_cort(),
                'A5': self.A5,
                'A6': self.A6,
                'A7': self.A7,
                'A8': self.A8, }


def main(h):
    global BYTE_INDEX

    BYTE_INDEX = 5

    A = structA()
    A.fill_struct(h)
    return A.get_cort()


h = (b'SICZ\x00\x00\x00\x04\x00\x00\x00+b\xca\xf1\xff\x83\xf2\xaf\x1d\x00\x00\x00c'
     b'T\xfc\xe8\x08+\x1a@<+\xb8\xba\xbf\xd2\x186\x8769\\txxb1`\xe2\xe1\x04'
     b'j-\xe3\xe5W\xe7\xbf\t\n8nH\xbcv_AGU\x8bB(\xd9`\x86z\x92\xbeSg\xb6\xf6\x00'
     b'\x02\x00/\x06}]DSo\x00\x02\x00?\xbd\xf9\xf7\xbb\x00\x00\x00\x02\x00\x00\x00'
     b'O\xa2G8\xeas\xdc=\xa5\th4\xf5')

print(main(h))
