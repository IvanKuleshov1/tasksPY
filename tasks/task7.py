def main(input):
    a = (input & 0b00000000000000000000001111111111) << 2
    b = (input & 0b00000000000000111111110000000000) << 14
    c = (input & 0b00111111111111000000000000000000) >> 6
    d = (input & 0b11000000000000000000000000000000) >> 30
    return a | b | c | d
