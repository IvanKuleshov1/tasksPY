import struct

BYTE_INDEX = 0


def my_repack(type, arr):
    global BYTE_INDEX
    BYTE_INDEX += len(arr)
    return struct.unpack(type, arr)[0]


class structE:
    def fill_struct(self, b):
        global BYTE_INDEX

        arr = []

        for i in range(4):
            arr.append(my_repack('>i', b[BYTE_INDEX: BYTE_INDEX + 4]))

        self.set_E1(arr)
        self.set_E2(my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4]))

        size = my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4])
        pointer = my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2])

        STOP_INDEX = BYTE_INDEX
        BYTE_INDEX = pointer

        arr1 = []

        for i in range(size):
            arr1.append(my_repack('>B', b[BYTE_INDEX: BYTE_INDEX + 1]))

        self.set_E3(arr1)

        BYTE_INDEX = STOP_INDEX

        return self

    def set_E1(self, a):
        self.E1 = a

    def set_E2(self, a):
        self.E2 = a

    def set_E3(self, a):
        self.E3 = a

    def get_cort(self):
        return {'E1': self.E1, 'E2': self.E2, 'E3': self.E3}


class structD:
    def fill_struct(self, b):
        global BYTE_INDEX

        self.set_D1(my_repack('>b', b[BYTE_INDEX: BYTE_INDEX + 1]))
        self.set_D2(my_repack('>B', b[BYTE_INDEX: BYTE_INDEX + 1]))

        size = my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4])
        pointer = my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2])

        STOP_INDEX = BYTE_INDEX
        BYTE_INDEX = pointer

        arr = []

        for i in range(size):
            arr.append(my_repack('>B', b[BYTE_INDEX: BYTE_INDEX + 1]))

        self.set_D3(arr)

        BYTE_INDEX = STOP_INDEX

        self.set_D4(my_repack('>b', b[BYTE_INDEX: BYTE_INDEX + 1]))
        self.set_D5(my_repack('>Q', b[BYTE_INDEX: BYTE_INDEX + 8]))

        return self

    def set_D1(self, a):
        self.D1 = a

    def set_D2(self, a):
        self.D2 = a

    def set_D3(self, a):
        self.D3 = a

    def set_D4(self, a):
        self.D4 = a

    def set_D5(self, a):
        self.D5 = a

    def get_cort(self):
        return {'D1': self.D1,
                'D2': self.D2,
                'D3': self.D3,
                'D4': self.D4,
                'D5': self.D5}


class structC:
    def fill_struct(self, b):
        global BYTE_INDEX

        self.set_C1(structD().fill_struct(b))
        self.set_C2(my_repack('>i', b[BYTE_INDEX: BYTE_INDEX + 4]))
        self.set_C3(my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2]))

        return self

    def set_C1(self, a):
        self.C1 = a

    def set_C2(self, a):
        self.C2 = a

    def set_C3(self, a):
        self.C3 = a

    def get_cort(self):
        return {'C1': self.C1.get_cort(),
                'C2': self.C2,
                'C3': self.C3}


class structB:
    def fill_struct(self, b):
        global BYTE_INDEX

        arr_C = []

        for i in range(2):
            arr_C.append(structC().fill_struct(b))

        self.set_B1(arr_C)

        size = my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2])

        pointer = my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4])

        STOP_INDEX = BYTE_INDEX
        BYTE_INDEX = pointer

        arr_uint8 = []

        for i in range(size):
            arr_uint8.append(my_repack('>B', b[BYTE_INDEX: BYTE_INDEX + 1]))

        self.set_B2(arr_uint8)

        BYTE_INDEX = STOP_INDEX

        self.set_B3(my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4]))
        self.set_B4(my_repack('>i', b[BYTE_INDEX: BYTE_INDEX + 4]))
        self.set_B5(my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2]))

        pointer = my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2])

        STOP_INDEX = BYTE_INDEX
        BYTE_INDEX = pointer

        self.set_B6(structE().fill_struct(b))

        BYTE_INDEX = STOP_INDEX

        self.set_B7(my_repack('>b', b[BYTE_INDEX: BYTE_INDEX + 1]))

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

    def set_B7(self, a):
        self.B7 = a

    def get_cort(self):
        arr = []

        for i in self.B1:
            arr.append(i.get_cort())

        return {'B1': arr,
                'B2': self.B2,
                'B3': self.B3,
                'B4': self.B4,
                'B5': self.B5,
                'B6': self.B6.get_cort(),
                'B7': self.B7}


class structA:
    def fill_struct(self, b):
        global BYTE_INDEX

        self.set_A1(my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2]))
        self.set_A2(my_repack('>H', b[BYTE_INDEX: BYTE_INDEX + 2]))

        pointer = my_repack('>I', b[BYTE_INDEX: BYTE_INDEX + 4])

        STOP_INDEX = BYTE_INDEX
        BYTE_INDEX = pointer

        self.set_A3(structB().fill_struct(b))

        BYTE_INDEX = STOP_INDEX

        return self

    def set_A1(self, a):
        self.A1 = a

    def set_A2(self, a):
        self.A2 = a

    def set_A3(self, a):
        self.A3 = a

    def get_cort(self):
        return {'A1': self.A1,
                'A2': self.A2,
                'A3': self.A3.get_cort()}


def main(h):
    global BYTE_INDEX

    BYTE_INDEX = 5

    A = structA()
    A.fill_struct(h)
    return A.get_cort()


h = (b'CCGV\x9f\n\x118{\x00\x00\x003\x17\x11\xa6\x9a\x8f\xc2\x98\x9e\x92\xfb\xc2'
     b'\xa8\xd9\xdb\xd1c:E\x01\xa1\x16/\xc1cs\x95N\x8b>\xe6\x97\xb7\x00\x00\x00'
     b'\x03\x00\x16&\x05\x00\x00\x00\x03\x00\r\x1b\x9ar\xd2\x87\x1ani\x8c\xbck\x95c'
     b'\x11\x00\xf0\xb4\x00\x00\x00\x03\x00\x10(U\xbb\xde<\xddW\xd1\x9eG'
     b'b\xfe\xdf\xf7O\x00\x03\x00\x00\x00\x13U\xd6\x11\x85\xe6\xf2\x10Qg'
     b'\x0e\x00\x19\x87')

print(main(h))
