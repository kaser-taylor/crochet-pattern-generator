def find_c_inc(m1, m2):
    c = (m1 - m2) / 2

    return c

def find_c_dec(m1, m2):
    c = (m2 - m1) / 2

    return c

def find_a_inc(c, length):
    a = (-c / (-(length ** 2)))

    return a

def find_a_dec(c, length):
    a = (-c / (length ** 2))

    return a

def find_width_inc(a, length, i, stitch_height, c):
    length = (length) + (i * stitch_height)
    y = a * (-(length ** 2)) + c

    return y

