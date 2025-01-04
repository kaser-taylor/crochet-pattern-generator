def find_c(length, stitch_height, slope):
    x = length // stitch_height
    c = -slope * (x ** 2)

    return c

def find_c(m1, m2,  i_d):
    c = 0
    if i_d == True:
        c = (m2 - m1) / 2
    else:
        c = (m1 - m2) / 2
    
    return c
